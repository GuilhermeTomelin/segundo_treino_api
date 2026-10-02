import requests
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Consulta de Cotações",
    page_icon="💱",
    layout="centered"
)

st.title("💱 Consulta de Cotações de Moedas")
st.write("Acompanhe o valor atualizado de moedas e criptomoedas em tempo real.")

# Mapeamento do menu de moedas para um Selectbox
opcoes_moedas = {
    "Dólar Americano (USD-BRL)": "USD-BRL",
    "Euro (EUR-BRL)": "EUR-BRL",
    "Libra Esterlina (GBP-BRL)": "GBP-BRL",
    "Peso Argentino (ARS-BRL)": "ARS-BRL",
    "Bitcoin (BTC-BRL)": "BTC-BRL",
    "Ethereum (ETH-BRL)": "ETH-BRL",
    "Outra moeda (digitar manualmente)": "OUTRA"
}

# Interface para seleção da moeda
escolha = st.selectbox("Escolha uma opção do menu:", list(opcoes_moedas.keys()))

if opcoes_moedas[escolha] == "OUTRA":
    moeda_desejada = st.text_input(
        "Digite o par de moedas desejado (ex: CAD-BRL, JPY-BRL):",
        value=""
    ).strip().upper()
else:
    moeda_desejada = opcoes_moedas[escolha]


def consultar_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.json(), None
        elif resposta.status_code == 404:
            erro = resposta.json()
            status = erro.get("status")
            code = erro.get("code")
            message = erro.get("message")
            return None, f"Erro {code} ({status}): {message}"
        else:
            return None, f"Requisição não feita. Status: {resposta.status_code}"
    except Exception as e:
        return None, f"Erro ao conectar com o serviço: {e}"


# Botão para realizar a consulta
if st.button("Consultar Cotação", type="primary"):
    if not moeda_desejada:
        st.warning("Por favor, informe ou selecione uma moeda válida.")
    else:
        with st.spinner("Buscando dados na API..."):
            dados_api, erro_msg = consultar_moeda(moeda_desejada)

        if dados_api:
            chave = moeda_desejada.replace("-", "")

            if chave in dados_api:
                info = dados_api[chave]
                valor = float(info["bid"])
                variacao = float(info.get("pctChange", 0))
                nome = info.get("name", moeda_desejada)

                st.success("Requisição bem-sucedida!")

                # Exibição visual do valor usando st.metric
                st.metric(
                    label=f"Cotação Atual ({nome})",
                    value=f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                    delta=f"{variacao:.2f}% (24h)"
                )

                # Exibe o JSON de retorno expandível para depuração
                with st.expander("Ver retorno completo da API"):
                    st.json(info)
            else:
                st.error(f"Erro ao processar chave '{chave}' no retorno da API.")
        else:
            st.error(f"Erro ao consultar a moeda: {moeda_desejada}")
            st.error(erro_msg)
            st.info("Verifique se o formato está correto (exemplo: USD-BRL).")