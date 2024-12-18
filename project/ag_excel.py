import pandas as pd

def formatar_problema(problem):
    """
    Converte um dicionário de problema no formato 'SEND + MORE = MONEY'.
    """
    keys = list(problem.keys())
    return f"{keys[0]} + {keys[1]} = {keys[2]}"

def gerar_relatorio_excel(resultados_etapa1, melhores_configuracoes, resultados_etapa2, melhor_config, problema_facil):
    """
    Gera um relatório em formato Excel com:
    - Média aritmética de convergência.
    - Justificativa das 4 melhores configurações.
    - Melhor configuração global.
    """
    rows = []  # Dados para o Excel
    convergencias = []  # Armazena todas as taxas de convergência para cálculo da média

    # Adiciona os resultados da Etapa 1 no relatório
    for config, problem, conv_rate, tempo_medio in resultados_etapa1:
        convergencias.append(conv_rate)  # Armazena para cálculo da média
        rows.append({
            "Problema": formatar_problema(problem),  # Formata o problema como string
            "Configuração": f"TM={config[0]}, TC={config[1]}, Seleção={config[2]}, Crossover={config[3]}, Reinserção={config[4]}",
            "Taxa de Convergência (%)": f"{conv_rate * 100:.2f}",
            "Tempo Médio (s)": f"{tempo_medio:.4f}"
        })

    # Cálculo da média aritmética de convergência
    media_convergencia = sum(convergencias) / len(convergencias) if convergencias else 0

    # Adiciona justificativa para escolha das 4 melhores configurações
    rows.append({
        "Problema": "Justificativa",
        "Configuração": "Escolha das 4 Melhores Configurações",
        "Taxa de Convergência (%)": "-",
        "Tempo Médio (s)": "-",
        "Detalhes": "As 4 melhores configurações foram selecionadas com base na maior taxa de convergência "
                    "e no menor tempo médio de execução durante a Etapa 1, garantindo eficiência."
    })

    # Adiciona os resultados da Etapa 2 no relatório
    for config, problem, conv_rate, tempo_medio in resultados_etapa2:
        rows.append({
            "Problema": formatar_problema(problem),  # Formata o problema como string
            "Configuração": f"TM={config[0]}, TC={config[1]}, Seleção={config[2]}, Crossover={config[3]}, Reinserção={config[4]}",
            "Taxa de Convergência (%)": f"{conv_rate * 100:.2f}",
            "Tempo Médio (s)": f"{tempo_medio:.4f}"
        })

    # Adiciona justificativa para a escolha da melhor configuração global
    rows.append({
        "Problema": "Justificativa",
        "Configuração": "Escolha da Melhor Configuração Global",
        "Taxa de Convergência (%)": "-",
        "Tempo Médio (s)": "-",
        "Detalhes": "A melhor configuração global foi selecionada com base na maior taxa de convergência "
                    "e no menor tempo médio ao ser testada em todos os 5 problemas."
    })

    # Adiciona a configuração global escolhida
    rows.append({
        "Problema": problema_facil,
        "Configuração": f"TM={melhor_config[0]}, TC={melhor_config[1]}, Seleção={melhor_config[2]}, "
                        f"Crossover={melhor_config[3]}, Reinserção={melhor_config[4]}",
        "Taxa de Convergência (%)": "-",
        "Tempo Médio (s)": "-",
        "Detalhes": "Configuração Global"
    })

    # Adiciona a média global de convergência
    rows.append({
        "Problema": "Resumo",
        "Configuração": "Média Global de Convergência",
        "Taxa de Convergência (%)": f"{media_convergencia * 100:.2f}",
        "Tempo Médio (s)": "-"
    })

    # Cria o DataFrame e salva em Excel
    df = pd.DataFrame(rows)
    df.to_excel("relatorio_final.xlsx", index=False)
    print("Relatório gerado com sucesso: relatorio_final.xlsx")
