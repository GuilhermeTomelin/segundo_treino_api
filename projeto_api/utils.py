import streamlit as st
import numpy as np
import requests
import pandas as pd
import plotly.graph_objects as go
from data import DADOS_REGIONAIS

@st.cache_data(ttl=86400)
def obter_coordenadas_api_global(nome_pais):
    """Busca coordenadas exatas de qualquer país via API REST Countries."""
    try:
        url = f"https://restcountries.com/v3.1/name/{nome_pais}?fullText=false"
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()[0]
            return {"lat": data["latlng"][0], "lon": data["latlng"][1]}
    except Exception:
        pass
    return {"lat": 0.0, "lon": 0.0}

def obter_dados_pais(nome_pais):
    """Retorna os dados cadastrados ou gera fallback dinâmico via API."""
    if nome_pais in DADOS_REGIONAIS:
        return DADOS_REGIONAIS[nome_pais]
    
    coord = obter_coordenadas_api_global(nome_pais)
    lat, lon = coord["lat"], coord["lon"]
    
    return {
        "lat": lat, "lon": lon,
        "indicadores": {"segurança": 70, "saude": 75, "limpeza": 75},
        "estados": {
            "Região Principal": {
                "lat": lat, "lon": lon,
                "indicadores": {"segurança": 70, "saude": 75, "limpeza": 75},
                "descricao": f"Região central de {nome_pais}.",
                "pontos_criminalidade": [
                    {"nome": f"Centro de {nome_pais}", "lat": lat, "lon": lon, "segurança": 70},
                    {"nome": "Zona Norte", "lat": lat + 0.1, "lon": lon + 0.1, "segurança": 75}
                ],
                "pontos_turisticos": [
                    {"nome": f"Atração Principal de {nome_pais}", "categoria": "Histórico", "lat": lat, "lon": lon, "desc": "Ponto de interesse local."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": f"Capital de {nome_pais}", "estado": "Região Principal", "lat": lat, "lon": lon}
        ]
    }

def calcular_arco_voo(lat1, lon1, lat2, lon2, num_pontos=50):
    """Calcula a curva do voo entre dois pontos no mapa."""
    lats = np.linspace(lat1, lat2, num_pontos)
    lons = np.linspace(lon1, lon2, num_pontos)
    distancia = np.sqrt((lat2-lat1)**2 + (lon2-lon1)**2)
    offset = np.sin(np.linspace(0, np.pi, num_pontos)) * (distancia * 0.15)
    return lats + offset, lons

def gerar_mapa_regional(dados_pais, estado_sel, camada_sel):
    """Gera o mapa Plotly dinâmico com suporte para versões antigas e novas do Plotly."""
    has_scattermap = hasattr(go, "Scattermap")
    
    if estado_sel == "Todos (Nacional)":
        center_lat, center_lon, zoom_level = dados_pais["lat"], dados_pais["lon"], 4.5
    else:
        center_lat = dados_pais["estados"][estado_sel]["lat"]
        center_lon = dados_pais["estados"][estado_sel]["lon"]
        zoom_level = 7.5

    fig = go.Figure()

    # CAMADA 1: CRIMINALIDADE / SEGURANÇA
    if "Criminalidade" in camada_sel:
        lista_pontos = []
        for est_nome, est_info in dados_pais["estados"].items():
            if estado_sel in ["Todos (Nacional)", est_nome]:
                for pt in est_info.get("pontos_criminalidade", []):
                    lista_pontos.append(pt)

        if lista_pontos:
            df = pd.DataFrame(lista_pontos)
            kwargs = dict(
                lat=df["lat"], lon=df["lon"], mode='markers+text',
                marker=dict(
                    size=22, color=df["segurança"], colorscale='RdYlGn',
                    cmin=40, cmax=100, showscale=True,
                    colorbar=dict(title="Índice Segurança")
                ),
                text=df["nome"] + " (" + df["segurança"].astype(str) + "/100)",
                textposition="top center", hoverinfo="text", name="Segurança"
            )
            fig.add_trace(go.Scattermap(**kwargs) if has_scattermap else go.Scattermapbox(**kwargs))

    # CAMADA 2: PONTOS TURÍSTICOS
    elif "Turísticos" in camada_sel:
        lista_pts = []
        for est_nome, est_info in dados_pais["estados"].items():
            if estado_sel in ["Todos (Nacional)", est_nome]:
                for pt in est_info.get("pontos_turisticos", []):
                    lista_pts.append(pt)

        if lista_pts:
            df = pd.DataFrame(lista_pts)
            kwargs = dict(
                lat=df["lat"], lon=df["lon"], mode='markers+text',
                marker=dict(size=14, color='#38BDF8'),
                text=df["nome"] + " (" + df["categoria"] + ")",
                textposition="top center", name="Pontos Turísticos"
            )
            fig.add_trace(go.Scattermap(**kwargs) if has_scattermap else go.Scattermapbox(**kwargs))

    # CAMADA 3: ROTEIRO DE VIAGEM
    elif "Roteiro" in camada_sel:
        rot = [r for r in dados_pais["roteiro_nacional"] if estado_sel == "Todos (Nacional)" or r["estado"] == estado_sel]
        if len(rot) > 1:
            df = pd.DataFrame(rot).sort_values("ordem")
            kwargs = dict(
                lat=df["lat"], lon=df["lon"], mode='lines+markers+text',
                line=dict(width=4, color='#F59E0B'),
                marker=dict(size=12, color='#F59E0B'),
                text=df["ordem"].astype(str) + ". " + df["nome"],
                textposition="top right", name="Roteiro"
            )
            fig.add_trace(go.Scattermap(**kwargs) if has_scattermap else go.Scattermapbox(**kwargs))

    map_config = dict(
        style="open-street-map" if has_scattermap else "carto-darkmatter",
        center=dict(lat=center_lat, lon=center_lon),
        zoom=zoom_level
    )
    
    if has_scattermap:
        fig.update_layout(map=map_config, height=520, margin=dict(l=0, r=0, t=0, b=0))
    else:
        fig.update_layout(mapbox=map_config, height=520, margin=dict(l=0, r=0, t=0, b=0))

    return fig