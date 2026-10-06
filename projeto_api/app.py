import streamlit as st
from views.stage1_search import render_stage1
from views.stage2_regional import render_stage2

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="TravelPlanner - Inteligência de Viagem",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ESTILIZAÇÃO GLOBAL
st.markdown("""
<style>
    .search-card {
        background-color: rgba(15, 23, 42, 0.85);
        border: 2px solid #38BDF8;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
        margin: auto;
        max-width: 750px;
    }
    .metric-box {
        background-color: #1E293B;
        padding: 15px;
        border-radius: 12px;
        border-left: 4px solid #38BDF8;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ESTADO DA SESSÃO
if "estagio" not in st.session_state:
    st.session_state.estagio = 1

# Atualizado para "Japão" (presente na base de dados) para evitar o erro de lista
if "origem" not in st.session_state:
    st.session_state.origem = "Japão"

if "destino" not in st.session_state:
    st.session_state.destino = "Portugal"

if "voo_confirmado" not in st.session_state:
    st.session_state.voo_confirmado = None

# ROTEAMENTO DAS TELAS
if st.session_state.estagio == 1:
    render_stage1()
elif st.session_state.estagio == 2:
    render_stage2()