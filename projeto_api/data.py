# Base de dados regional com 20 países detalhados
DADOS_REGIONAIS = {
    "Brasil": {
        "lat": -14.2350, "lon": -51.9253,
        "indicadores": {"segurança": 62, "saude": 70, "limpeza": 75},
        "estados": {
            "São Paulo": {
                "lat": -23.5505, "lon": -46.6333,
                "indicadores": {"segurança": 68, "saude": 82, "limpeza": 78},
                "descricao": "Maior centro financeiro e cultural do país, repleto de gastronomia e arte.",
                "pontos_criminalidade": [
                    {"nome": "SP - Av. Paulista", "lat": -23.5615, "lon": -46.6560, "segurança": 78},
                    {"nome": "SP - Centro Histórico", "lat": -23.5489, "lon": -46.6388, "segurança": 52}
                ],
                "pontos_turisticos": [
                    {"nome": "MASP", "categoria": "Museu", "lat": -23.5614, "lon": -46.6559, "desc": "Museu de Arte de São Paulo."},
                    {"nome": "Parque Ibirapuera", "categoria": "Natureza", "lat": -23.5874, "lon": -46.6576, "desc": "O principal parque urbano da cidade."}
                ]
            },
            "Rio de Janeiro": {
                "lat": -22.9068, "lon": -43.1729,
                "indicadores": {"segurança": 55, "saude": 68, "limpeza": 72},
                "descricao": "Cidade Maravilhosa, mundialmente famosa pelas praias e paisagens naturais.",
                "pontos_criminalidade": [
                    {"nome": "Copacabana", "lat": -22.9711, "lon": -43.1825, "segurança": 70},
                    {"nome": "Lapa", "lat": -22.9133, "lon": -43.1806, "segurança": 58}
                ],
                "pontos_turisticos": [
                    {"nome": "Cristo Redentor", "categoria": "Monumento", "lat": -22.9519, "lon": -43.2105, "desc": "Uma das Sete Maravilhas do Mundo."},
                    {"nome": "Pão de Açúcar", "categoria": "Atração", "lat": -22.9492, "lon": -43.1545, "desc": "Passeio de bondinho com vista panorâmica."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "São Paulo", "estado": "São Paulo", "lat": -23.5505, "lon": -46.6333},
            {"ordem": 2, "nome": "Rio de Janeiro", "estado": "Rio de Janeiro", "lat": -22.9068, "lon": -43.1729}
        ]
    },
    "Japão": {
        "lat": 36.2048, "lon": 138.2529,
        "indicadores": {"segurança": 92, "saude": 90, "limpeza": 95},
        "estados": {
            "Kanto": {
                "lat": 35.6762, "lon": 139.6503,
                "indicadores": {"segurança": 90, "saude": 92, "limpeza": 96},
                "descricao": "Região metropolitana de Tóquio, centro tecnológico e cultural.",
                "pontos_criminalidade": [
                    {"nome": "Shinjuku", "lat": 35.6938, "lon": 139.7034, "segurança": 82},
                    {"nome": "Shibuya", "lat": 35.6580, "lon": 139.7016, "segurança": 88}
                ],
                "pontos_turisticos": [
                    {"nome": "Senso-ji", "categoria": "Templo", "lat": 35.7148, "lon": 139.7967, "desc": "Templo histórico em Asakusa."},
                    {"nome": "Torre de Tóquio", "categoria": "Monumento", "lat": 35.6586, "lon": 139.7454, "desc": "Ícone da arquitetura japonesa."}
                ]
            },
            "Kansai": {
                "lat": 34.6937, "lon": 135.5023,
                "indicadores": {"segurança": 89, "saude": 88, "limpeza": 93},
                "descricao": "Berço histórico e gastronómico do Japão.",
                "pontos_criminalidade": [
                    {"nome": "Namba (Osaka)", "lat": 34.6654, "lon": 135.5011, "segurança": 84}
                ],
                "pontos_turisticos": [
                    {"nome": "Fushimi Inari", "categoria": "Santuário", "lat": 34.9671, "lon": 135.7727, "desc": "Famoso pelos milhares de Torii."},
                    {"nome": "Castelo de Osaka", "categoria": "Histórico", "lat": 34.6873, "lon": 135.5262, "desc": "Fortaleza histórica do século XVI."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Tóquio", "estado": "Kanto", "lat": 35.6762, "lon": 139.6503},
            {"ordem": 2, "nome": "Quioto", "estado": "Kansai", "lat": 35.0116, "lon": 135.7681}
        ]
    },
    "Portugal": {
        "lat": 39.3999, "lon": -8.2245,
        "indicadores": {"segurança": 88, "saude": 82, "limpeza": 88},
        "estados": {
            "Lisboa": {
                "lat": 38.7223, "lon": -9.1393,
                "indicadores": {"segurança": 85, "saude": 84, "limpeza": 86},
                "descricao": "Capital histórica recheada de charme e cultura marítima.",
                "pontos_criminalidade": [
                    {"nome": "Baixa de Lisboa", "lat": 38.7115, "lon": -9.1390, "segurança": 85}
                ],
                "pontos_turisticos": [
                    {"nome": "Torre de Belém", "categoria": "Monumento", "lat": 38.6916, "lon": -9.2160, "desc": "Fortificação à beira do Rio Tejo."},
                    {"nome": "Castelo de São Jorge", "categoria": "Histórico", "lat": 38.7139, "lon": -9.1335, "desc": "Vista privilegiada sobre a cidade."}
                ]
            },
            "Porto": {
                "lat": 41.1579, "lon": -8.6291,
                "indicadores": {"segurança": 87, "saude": 83, "limpeza": 87},
                "descricao": "Famoso pelo vinho, arquitetura e rio Douro.",
                "pontos_criminalidade": [
                    {"nome": "Ribeira", "lat": 41.1408, "lon": -8.6130, "segurança": 84}
                ],
                "pontos_turisticos": [
                    {"nome": "Ponte Dom Luís I", "categoria": "Monumento", "lat": 41.1400, "lon": -8.6095, "desc": "Ícone da engenharia de ferro."},
                    {"nome": "Livraria Lello", "categoria": "Cultura", "lat": 41.1468, "lon": -8.6148, "desc": "Uma das livrarias mais bonitas do mundo."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Lisboa", "estado": "Lisboa", "lat": 38.7223, "lon": -9.1393},
            {"ordem": 2, "nome": "Porto", "estado": "Porto", "lat": 41.1579, "lon": -8.6291}
        ]
    },
    "Estados Unidos": {
        "lat": 37.0902, "lon": -95.7129,
        "indicadores": {"segurança": 72, "saude": 85, "limpeza": 80},
        "estados": {
            "Nova York": {
                "lat": 40.7128, "lon": -74.0060,
                "indicadores": {"segurança": 70, "saude": 88, "limpeza": 75},
                "descricao": "Metrópole global vibrante e cheia de atrativos.",
                "pontos_criminalidade": [
                    {"nome": "Times Square", "lat": 40.7580, "lon": -73.9855, "segurança": 78}
                ],
                "pontos_turisticos": [
                    {"nome": "Estátua da Liberdade", "categoria": "Monumento", "lat": 40.6892, "lon": -74.0445, "desc": "Símbolo histórico mundial."},
                    {"nome": "Central Park", "categoria": "Natureza", "lat": 40.7829, "lon": -73.9654, "desc": "Parque no centro de Manhattan."}
                ]
            },
            "Flórida": {
                "lat": 27.6648, "lon": -81.5158,
                "indicadores": {"segurança": 76, "saude": 82, "limpeza": 84},
                "descricao": "Clima ensolarado, parques temáticos e praias belíssimas.",
                "pontos_criminalidade": [
                    {"nome": "Miami Beach", "lat": 25.7907, "lon": -80.1300, "segurança": 78}
                ],
                "pontos_turisticos": [
                    {"nome": "Walt Disney World", "categoria": "Lazer", "lat": 28.3852, "lon": -81.5639, "desc": "Complexo de parques temáticos."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Nova York", "estado": "Nova York", "lat": 40.7128, "lon": -74.0060},
            {"ordem": 2, "nome": "Miami", "estado": "Flórida", "lat": 25.7617, "lon": -80.1918}
        ]
    },
    "França": {
        "lat": 46.2276, "lon": 2.2137,
        "indicadores": {"segurança": 80, "saude": 88, "limpeza": 82},
        "estados": {
            "Île-de-France": {
                "lat": 48.8566, "lon": 2.3522,
                "indicadores": {"segurança": 76, "saude": 88, "limpeza": 80},
                "descricao": "Região da capital Paris, repleta de arte e arquitetura icónica.",
                "pontos_criminalidade": [
                    {"nome": "Châtelet", "lat": 48.8584, "lon": 2.3470, "segurança": 70}
                ],
                "pontos_turisticos": [
                    {"nome": "Torre Eiffel", "categoria": "Monumento", "lat": 48.8584, "lon": 2.2945, "desc": "Símbolo de Paris e da França."},
                    {"nome": "Museu do Louvre", "categoria": "Museu", "lat": 48.8606, "lon": 2.3376, "desc": "Maior museu de arte do mundo."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Paris", "estado": "Île-de-France", "lat": 48.8566, "lon": 2.3522}
        ]
    },
    "Itália": {
        "lat": 41.8719, "lon": 12.5674,
        "indicadores": {"segurança": 82, "saude": 85, "limpeza": 80},
        "estados": {
            "Lácio": {
                "lat": 41.9028, "lon": 12.4964,
                "indicadores": {"segurança": 78, "saude": 84, "limpeza": 78},
                "descricao": "Região da milenar cidade de Roma.",
                "pontos_criminalidade": [
                    {"nome": "Estação Termini", "lat": 41.9010, "lon": 12.5018, "segurança": 65}
                ],
                "pontos_turisticos": [
                    {"nome": "Coliseu", "categoria": "Histórico", "lat": 41.8902, "lon": 12.4922, "desc": "Anfiteatro romano antigo."},
                    {"nome": "Fontana di Trevi", "categoria": "Monumento", "lat": 41.9009, "lon": 12.4833, "desc": "Famosa fonte barroca."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Roma", "estado": "Lácio", "lat": 41.9028, "lon": 12.4964}
        ]
    },
    "Espanha": {
        "lat": 40.4637, "lon": -3.7492,
        "indicadores": {"segurança": 85, "saude": 88, "limpeza": 85},
        "estados": {
            "Madri": {
                "lat": 40.4168, "lon": -3.7038,
                "indicadores": {"segurança": 84, "saude": 88, "limpeza": 86},
                "descricao": "Capital vibrante no centro da Península Ibérica.",
                "pontos_criminalidade": [
                    {"nome": "Puerta del Sol", "lat": 40.4169, "lon": -3.7035, "segurança": 80}
                ],
                "pontos_turisticos": [
                    {"nome": "Museu do Prado", "categoria": "Museu", "lat": 40.4138, "lon": -3.6921, "desc": "Galeria de arte de prestígio internacional."},
                    {"nome": "Parque do Retiro", "categoria": "Natureza", "lat": 40.4153, "lon": -3.6845, "desc": "Extenso parque urbano."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Madri", "estado": "Madri", "lat": 40.4168, "lon": -3.7038}
        ]
    },
    "Alemanha": {
        "lat": 51.1657, "lon": 10.4515,
        "indicadores": {"segurança": 86, "saude": 90, "limpeza": 89},
        "estados": {
            "Baviera": {
                "lat": 48.1351, "lon": 11.5820,
                "indicadores": {"segurança": 88, "saude": 91, "limpeza": 90},
                "descricao": "Famosa pelas tradições, Alpes e a cidade de Munique.",
                "pontos_criminalidade": [
                    {"nome": "Marienplatz", "lat": 48.1374, "lon": 11.5755, "segurança": 88}
                ],
                "pontos_turisticos": [
                    {"nome": "Castelo de Neuschwanstein", "categoria": "Histórico", "lat": 47.5576, "lon": 10.7498, "desc": "Castelo de conto de fadas nos Alpes."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Munique", "estado": "Baviera", "lat": 48.1351, "lon": 11.5820}
        ]
    },
    "Reino Unido": {
        "lat": 55.3781, "lon": -3.4360,
        "indicadores": {"segurança": 83, "saude": 86, "limpeza": 84},
        "estados": {
            "Inglaterra": {
                "lat": 51.5074, "lon": -0.1278,
                "indicadores": {"segurança": 81, "saude": 86, "limpeza": 83},
                "descricao": "Sede da capital Londres e marcos históricos globais.",
                "pontos_criminalidade": [
                    {"nome": "Piccadilly Circus", "lat": 51.5100, "lon": -0.1340, "segurança": 76}
                ],
                "pontos_turisticos": [
                    {"nome": "Big Ben", "categoria": "Monumento", "lat": 51.5007, "lon": -0.1246, "desc": "Torre do relógio do Palácio de Westminster."},
                    {"nome": "London Eye", "categoria": "Atração", "lat": 51.5033, "lon": -0.1195, "desc": "Roda-gigante panorâmica no Tamisa."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Londres", "estado": "Inglaterra", "lat": 51.5074, "lon": -0.1278}
        ]
    },
    "Argentina": {
        "lat": -38.4161, "lon": -63.6167,
        "indicadores": {"segurança": 65, "saude": 75, "limpeza": 78},
        "estados": {
            "Buenos Aires": {
                "lat": -34.6037, "lon": -58.3816,
                "indicadores": {"segurança": 68, "saude": 78, "limpeza": 80},
                "descricao": "Capital charmosa com rica arquitetura europeia e cultura do tango.",
                "pontos_criminalidade": [
                    {"nome": "Caminito", "lat": -34.6394, "lon": -58.3628, "segurança": 65}
                ],
                "pontos_turisticos": [
                    {"nome": "Obelisco", "categoria": "Monumento", "lat": -34.6037, "lon": -58.3816, "desc": "Monumento no centro da cidade."},
                    {"nome": "Teatro Colón", "categoria": "Cultura", "lat": -34.6011, "lon": -58.3831, "desc": "Casa de ópera de acústica renomada."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Buenos Aires", "estado": "Buenos Aires", "lat": -34.6037, "lon": -58.3816}
        ]
    },
    "Canadá": {
        "lat": 56.1304, "lon": -106.3468,
        "indicadores": {"segurança": 91, "saude": 89, "limpeza": 92},
        "estados": {
            "Ontário": {
                "lat": 43.6532, "lon": -79.3832,
                "indicadores": {"segurança": 90, "saude": 90, "limpeza": 92},
                "descricao": "Província que abriga Toronto e as Cataratas do Niágara.",
                "pontos_criminalidade": [
                    {"nome": "Downtown Toronto", "lat": 43.6532, "lon": -79.3832, "segurança": 88}
                ],
                "pontos_turisticos": [
                    {"nome": "CN Tower", "categoria": "Monumento", "lat": 43.6426, "lon": -79.3871, "desc": "Torre de comunicação com vista panorâmica."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Toronto", "estado": "Ontário", "lat": 43.6532, "lon": -79.3832}
        ]
    },
    "Austrália": {
        "lat": -25.2744, "lon": 133.7751,
        "indicadores": {"segurança": 89, "saude": 88, "limpeza": 91},
        "estados": {
            "Nova Gales do Sul": {
                "lat": -33.8688, "lon": 151.2093,
                "indicadores": {"segurança": 88, "saude": 89, "limpeza": 90},
                "descricao": "Região de Sydney com praias e arquitetura moderna.",
                "pontos_criminalidade": [
                    {"nome": "Kings Cross", "lat": -33.8742, "lon": 151.2222, "segurança": 80}
                ],
                "pontos_turisticos": [
                    {"nome": "Opera House", "categoria": "Monumento", "lat": -33.8568, "lon": 151.2153, "desc": "Ícone mundial das artes cénicas."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Sydney", "estado": "Nova Gales do Sul", "lat": -33.8688, "lon": 151.2093}
        ]
    },
    "México": {
        "lat": 23.6345, "lon": -102.5528,
        "indicadores": {"segurança": 58, "saude": 72, "limpeza": 70},
        "estados": {
            "Cidade do México": {
                "lat": 19.4326, "lon": -99.1332,
                "indicadores": {"segurança": 60, "saude": 75, "limpeza": 72},
                "descricao": "Capital histórica com ruínas astecas e rica gastronomia.",
                "pontos_criminalidade": [
                    {"nome": "Zócalo", "lat": 19.4326, "lon": -99.1332, "segurança": 62}
                ],
                "pontos_turisticos": [
                    {"nome": "Museu de Antropologia", "categoria": "Museu", "lat": 19.4260, "lon": -99.1863, "desc": "Acervo sobre as civilizações pré-colombianas."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Cidade do México", "estado": "Cidade do México", "lat": 19.4326, "lon": -99.1332}
        ]
    },
    "Chile": {
        "lat": -35.6751, "lon": -71.5430,
        "indicadores": {"segurança": 78, "saude": 80, "limpeza": 82},
        "estados": {
            "Região Metropolitana": {
                "lat": -33.4489, "lon": -70.6693,
                "indicadores": {"segurança": 76, "saude": 82, "limpeza": 80},
                "descricao": "Região de Santiago cercada pelas cordilheiras dos Andes.",
                "pontos_criminalidade": [
                    {"nome": "Plaza de Armas", "lat": -33.4378, "lon": -70.6504, "segurança": 70}
                ],
                "pontos_turisticos": [
                    {"nome": "Cerro San Cristóbal", "categoria": "Natureza", "lat": -33.4253, "lon": -70.6331, "desc": "Miradouro natural da cidade."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Santiago", "estado": "Região Metropolitana", "lat": -33.4489, "lon": -70.6693}
        ]
    },
    "Suíça": {
        "lat": 46.8182, "lon": 8.2275,
        "indicadores": {"segurança": 95, "saude": 94, "limpeza": 97},
        "estados": {
            "Zurique": {
                "lat": 47.3769, "lon": 8.5417,
                "indicadores": {"segurança": 96, "saude": 95, "limpeza": 98},
                "descricao": "Centro financeiro alpino com paisagens exuberantes.",
                "pontos_criminalidade": [
                    {"nome": "Hauptbahnhof", "lat": 47.3779, "lon": 8.5403, "segurança": 90}
                ],
                "pontos_turisticos": [
                    {"nome": "Lago de Zurique", "categoria": "Natureza", "lat": 47.3622, "lon": 8.5461, "desc": "Belo lago cercado por montanhas."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Zurique", "estado": "Zurique", "lat": 47.3769, "lon": 8.5417}
        ]
    },
    "Holanda": {
        "lat": 52.1326, "lon": 5.2913,
        "indicadores": {"segurança": 88, "saude": 89, "limpeza": 90},
        "estados": {
            "Holanda do Norte": {
                "lat": 52.3676, "lon": 4.9041,
                "indicadores": {"segurança": 86, "saude": 89, "limpeza": 88},
                "descricao": "Região de Amesterdão com canais históricos e museus.",
                "pontos_criminalidade": [
                    {"nome": "Red Light District", "lat": 52.3731, "lon": 4.8966, "segurança": 78}
                ],
                "pontos_turisticos": [
                    {"nome": "Rijksmuseum", "categoria": "Museu", "lat": 52.3600, "lon": 4.8852, "desc": "Museu nacional com mestres holandeses."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Amesterdão", "estado": "Holanda do Norte", "lat": 52.3676, "lon": 4.9041}
        ]
    },
    "África do Sul": {
        "lat": -30.5595, "lon": 22.9375,
        "indicadores": {"segurança": 52, "saude": 68, "limpeza": 72},
        "estados": {
            "Cabo Ocidental": {
                "lat": -33.9249, "lon": 18.4241,
                "indicadores": {"segurança": 62, "saude": 75, "limpeza": 80},
                "descricao": "Região da Cidade do Cabo, praias e montanhas impressionantes.",
                "pontos_criminalidade": [
                    {"nome": "CBD Cape Town", "lat": -33.9249, "lon": 18.4241, "segurança": 58}
                ],
                "pontos_turisticos": [
                    {"nome": "Table Mountain", "categoria": "Natureza", "lat": -33.9628, "lon": 18.4098, "desc": "Montanha de topo plano icónica."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Cidade do Cabo", "estado": "Cabo Ocidental", "lat": -33.9249, "lon": 18.4241}
        ]
    },
    "Grécia": {
        "lat": 39.0742, "lon": 21.8243,
        "indicadores": {"segurança": 82, "saude": 78, "limpeza": 80},
        "estados": {
            "Ática": {
                "lat": 37.9838, "lon": 23.7275,
                "indicadores": {"segurança": 80, "saude": 80, "limpeza": 78},
                "descricao": "Região de Atenas, o berço da civilização ocidental.",
                "pontos_criminalidade": [
                    {"nome": "Praça Omonia", "lat": 37.9842, "lon": 23.7281, "segurança": 68}
                ],
                "pontos_turisticos": [
                    {"nome": "Acrópole de Atenas", "categoria": "Histórico", "lat": 37.9715, "lon": 23.7257, "desc": "Complexo arquitetónico da Grécia Antiga."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Atenas", "estado": "Ática", "lat": 37.9838, "lon": 23.7275}
        ]
    },
    "Egito": {
        "lat": 26.8206, "lon": 30.8025,
        "indicadores": {"segurança": 60, "saude": 62, "limpeza": 65},
        "estados": {
            "Cairo": {
                "lat": 30.0444, "lon": 31.2357,
                "indicadores": {"segurança": 62, "saude": 65, "limpeza": 60},
                "descricao": "Metrópole milenar ao longo do rio Nilo.",
                "pontos_criminalidade": [
                    {"nome": "Centro do Caiu", "lat": 30.0444, "lon": 31.2357, "segurança": 60}
                ],
                "pontos_turisticos": [
                    {"nome": "Pirâmides de Gizé", "categoria": "Histórico", "lat": 29.9792, "lon": 31.1342, "desc": "Monumentos funerários do Antigo Egito."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Cairo", "estado": "Cairo", "lat": 30.0444, "lon": 31.2357}
        ]
    },
    "Tailândia": {
        "lat": 15.8700, "lon": 100.9925,
        "indicadores": {"segurança": 75, "saude": 78, "limpeza": 72},
        "estados": {
            "Bangkok": {
                "lat": 13.7563, "lon": 100.5018,
                "indicadores": {"segurança": 74, "saude": 80, "limpeza": 70},
                "descricao": "Capital vibrante com templos dourados e vida noturna agitada.",
                "pontos_criminalidade": [
                    {"nome": "Khao San Road", "lat": 13.7589, "lon": 100.4972, "segurança": 70}
                ],
                "pontos_turisticos": [
                    {"nome": "Grande Palácio", "categoria": "Histórico", "lat": 13.7500, "lon": 100.4913, "desc": "Residência oficial dos reis do Sião."}
                ]
            }
        },
        "roteiro_nacional": [
            {"ordem": 1, "nome": "Bangkok", "estado": "Bangkok", "lat": 13.7563, "lon": 100.5018}
        ]
    }
}