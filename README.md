# ✈️ TravelPlanner — Inteligência Global de Viagens

O **TravelPlanner** é uma aplicação web interativa desenvolvida em Python com **Streamlit** e **Plotly**, projetada para auxiliar viajantes na busca de voos, mapeamento de rotas globais em mapas 3D/geográficos e análise detalhada de segurança, saúde, limpeza e atrações turísticas regionais de mais de 20 países.
---
## 📌 Funcionalidades Principais

- **Mapeamento de Rotas Globais:** Visualização de arcos de voo interativos em mapas mundiais renderizados com Plotly.
- **Seleção Dinâmica de Voos:** Comparação de rotas diretas, com escalas e opções econômicas.
- **Análise Regional & Indicadores:** Painel interativo por estado/região mostrando índices de **Segurança**, **Saúde** e **Limpeza**.
- **Pontos de Interesse e Alertas:** Exibição geolocalizada de atrações turísticas (com categorias) e zonas com alertas de atenção.
- **Arquitetura Modularizada:** Estrutura limpa baseada em views, componentes utilitários e dados centralizados.
---
## 📂 Estrutura do Projeto

```text
projeto_api/
│
├── app.py                      # Ponto de entrada da aplicação (Roteamento de telas)
├── data.py                     # Base de dados regional detalhada (20+ Países)
├── utils.py                    # Funções auxiliares (Cálculo de arcos, filtros)
├── README.md                   # Documentação do projeto
└── views/                      # Camada de Apresentação (Telas)
    ├── stage1_search.py        # Pesquisa de voos e mapa global
    └── stage2_regional.py      # Visão detalhada por país/estado e indicadores
```
---
## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/)** — Linguagem principal
* **[Streamlit](https://streamlit.io/)** — Framework web para aplicações de dados
* **[Plotly](https://plotly.com/python/)** — Visualização de mapas interativos e gráficos
---

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado na sua máquina.

### 1. Clonar o repositório

```bash
git clone https://github.com/GuilhermeTomelin/sistema_viagens_streamlite_.git

cd sistema_viagens_streamlite_

### 2. Instalar as dependências

```bash
pip install streamlit plotly

```

### 3. Executar a aplicação

```bash
streamlit run app.py

```

Acesse a aplicação no seu navegador pelo endereço local: `http://localhost:8501`.

---

## 🔮 Próximos Passos (Roadmap)

* [ ] Integrar a **REST Countries API** para consumo dinâmico de dados geográficos globais.
* [ ] Conectar com APIs reais de voos (ex: **Amadeus Self-Service API**).
* [ ] Implementar exportação de roteiros em formato PDF.
* [ ] Adicionar sistema de autenticação e histórico de pesquisas salvas.

---

## 📜 Licença

Este projeto está sob a licença [MIT](https://www.google.com/search?q=LICENSE) — sinta-se à vontade para utilizar, modificar e distribuir.

```

```
