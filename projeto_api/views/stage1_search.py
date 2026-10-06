import streamlit as st
import plotly.graph_objects as go
from utils import obter_dados_pais, calcular_arco_voo
from data import DADOS_REGIONAIS

def render_stage1():
    st.title("✈️ TravelPlanner — Inteligência Global de Viagens")
    st.caption("Selecione a origem e o destino para mapear rotas e encontrar opções de voo.")

    with st.container():
        st.markdown('<div class="search-card">', unsafe_allow_html=True)
        st.subheader("🔍 Para onde deseja viajar?")
        col_orig, col_dest = st.columns(2)
        
        lista_paises = list(DADOS_REGIONAIS.keys())
        
        # Proteção para garantir que o país de origem existe na lista
        index_origem = lista_paises.index(st.session_state.origem) if st.session_state.origem in lista_paises else 0

        with col_orig:
            origem = st.selectbox("Local de Origem:", lista_paises, index=index_origem)
        with col_dest:
            destinos_disp = [p for p in lista_paises if p != origem]
            index_destino = 0
            destino = st.selectbox("Destino Desejado:", destinos_disp, index=index_destino)

        if st.button("✈️ Pesquisar Voos e Mapear Rota", use_container_width=True, type="primary"):
            st.session_state.origem = origem
            st.session_state.destino = destino

        st.markdown('</div>', unsafe_allow_html=True)

    dados_origem = obter_dados_pais(st.session_state.origem)
    dados_destino = obter_dados_pais(st.session_state.destino)

    lats_arco, lons_arco = calcular_arco_voo(
        dados_origem["lat"], dados_origem["lon"],
        dados_destino["lat"], dados_destino["lon"]
    )

    fig_mundi = go.Figure()
    fig_mundi.add_trace(go.Scattergeo(
        lat=[dados_origem["lat"], dados_destino["lat"]],
        lon=[dados_origem["lon"], dados_destino["lon"]],
        mode='markers+text',
        text=[st.session_state.origem, st.session_state.destino],
        textposition="top center",
        marker=dict(size=12, color=['#10B981', '#EF4444'])
    ))

    fig_mundi.add_trace(go.Scattergeo(
        lat=lats_arco, lon=lons_arco, mode='lines',
        line=dict(width=3, color='#38BDF8')
    ))

    fig_mundi.update_layout(
        geo=dict(
            projection_type="natural earth", showland=True, landcolor="#1E293B",
            showocean=True, oceancolor="#0F172A", showcountries=True, countrycolor="#334155",
            center=dict(lat=(dados_origem["lat"]+dados_destino["lat"])/2, lon=(dados_origem["lon"]+dados_destino["lon"])/2),
            projection_scale=1.8
        ),
        height=420, margin=dict(l=0, r=0, t=0, b=0)
    )

    st.plotly_chart(fig_mundi, use_container_width=True)

    st.markdown("### 🛫 Opções de Voos Encontradas")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-box"><h4>Linha 1: Voo Direto</h4><p><b>Preço:</b> R$ 6.850,00</p><p><b>Duração:</b> 22h 10m</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar Voo Direto", key="v1"):
            st.session_state.voo_confirmado = "Voo Direto (Linha 1)"
            st.session_state.estagio = 2
            st.rerun()

    with col2:
        st.markdown('<div class="metric-box"><h4>Linha 2: 1 Conexão</h4><p><b>Preço:</b> R$ 5.420,00</p><p><b>Duração:</b> 25h 40m</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar 1 Escala", key="v2"):
            st.session_state.voo_confirmado = "1 Escala (Linha 2)"
            st.session_state.estagio = 2
            st.rerun()

    with col3:
        st.markdown('<div class="metric-box"><h4>Linha 3: Econômico</h4><p><b>Preço:</b> R$ 4.910,00</p><p><b>Duração:</b> 29h 15m</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar Econômico", key="v3"):
            st.session_state.voo_confirmado = "Econômico (Linha 3)"
            st.session_state.estagio = 2
            st.rerun()