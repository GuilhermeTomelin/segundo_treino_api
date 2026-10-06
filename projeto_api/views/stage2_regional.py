import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils import obter_dados_pais, gerar_mapa_regional

def render_stage2():
    destino = st.session_state.destino
    dados_pais = obter_dados_pais(destino)

    st.sidebar.title(f"📍 Destino: {destino}")
    st.sidebar.caption(f"Voo: {st.session_state.voo_confirmado}")

    if st.sidebar.button("⬅️ Alterar Rota / Voltar"):
        st.session_state.estagio = 1
        st.rerun()

    st.sidebar.markdown("---")
    
    # SELEÇÃO EXCLUSIVA DE CAMADA (RADIO BUTTON)
    camada_sel = st.sidebar.radio(
        "🎛️ Camada Ativa no Mapa:",
        [
            "🛡️ Criminalidade (Pontos Detalhados)",
            "🏛️ Pontos Turísticos",
            "🗺️️ Roteiro 'Ligue os Pontos'"
        ]
    )

    st.sidebar.markdown("---")
    
    # FILTRO DE ESTADO
    lista_estados = ["Todos (Nacional)"] + list(dados_pais["estados"].keys())
    estado_sel = st.sidebar.selectbox("🔍 Filtrar Visão por Estado/Região:", lista_estados)

    # MAPA REGIONAL
    st.title(f"🗾 Exploração Regional: {destino}")
    if estado_sel != "Todos (Nacional)":
        st.info(f"📍 Visualizando dados exclusivos de: **{estado_sel}**")

    fig_mapa = gerar_mapa_regional(dados_pais, estado_sel, camada_sel)
    st.plotly_chart(fig_mapa, use_container_width=True)

    # EXTRAÇÃO DE INDICADORES REATIVOS (PAÍS VS ESTADO)
    if estado_sel == "Todos (Nacional)":
        indicadores = dados_pais["indicadores"]
        titulo_secao = f"📊 Indicadores Nacionais: {destino}"
        descricao = f"Exibindo a média nacional de segurança, saúde e limpeza de {destino}."
    else:
        dados_est = dados_pais["estados"][estado_sel]
        indicadores = dados_est["indicadores"]
        titulo_secao = f"📊 Indicadores do Estado: {estado_sel} ({destino})"
        descricao = dados_est.get("descricao", "Informações regionais atualizadas.")

    st.markdown("---")
    st.subheader(titulo_secao)
    st.write(descricao)

    col_radar, col_barras = st.columns([1, 1])

    with col_radar:
        categories = ['Segurança', 'Saúde', 'Limpeza']
        values = [indicadores['segurança'], indicadores['saude'], indicadores['limpeza']]

        fig_radar = go.Figure(data=go.Scatterpolar(
            r=values, theta=categories, fill='toself',
            fillcolor='rgba(56, 189, 248, 0.4)',
            line=dict(color='#38BDF8', width=2)
        ))

        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False, height=300, margin=dict(l=30, r=30, t=20, b=20)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_barras:
        st.markdown("### 📋 Métrica Detalhada")
        st.markdown(f"**🛡️ Nível de Segurança:** {indicadores['segurança']}/100")
        st.progress(indicadores['segurança'] / 100)
        
        st.markdown(f"**🏥 Cuidados de Saúde:** {indicadores['saude']}/100")
        st.progress(indicadores['saude'] / 100)
        
        st.markdown(f"**🌿 Limpeza e Meio Ambiente:** {indicadores['limpeza']}/100")
        st.progress(indicadores['limpeza'] / 100)

    # SECCÃO DE PONTOS TURÍSTICOS DINÂMICOS DO ESTADO
    st.markdown("---")
    st.subheader(f"🏛️ Locais Turísticos em {estado_sel if estado_sel != 'Todos (Nacional)' else destino}")

    pontos_exibir = []
    for est_nome, est_info in dados_pais["estados"].items():
        if estado_sel in ["Todos (Nacional)", est_nome]:
            for pt in est_info.get("pontos_turisticos", []):
                pt_copy = pt.copy()
                pt_copy["estado"] = est_nome
                pontos_exibir.append(pt_copy)

    if pontos_exibir:
        cols = st.columns(len(pontos_exibir) if len(pontos_exibir) <= 3 else 3)
        for idx, pt in enumerate(pontos_exibir):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="metric-box">
                    <h4>{pt['nome']}</h4>
                    <p><b>Estado:</b> {pt['estado']}</p>
                    <p><b>Categoria:</b> {pt['categoria']}</p>
                    <p>{pt['desc']}</p>
                </div>
                """, unsafe_allow_html=True)