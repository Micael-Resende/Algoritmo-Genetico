from multiprocessing import Pool, cpu_count
from ag_problem import PROBLEMAS
from ag_core import AlgoritmoGenetico
from ag_config import NUM_EXECUCOES, TAXAS_MUTACAO, TAXAS_CRUZAMENTO, SELECAO_METODOS, CROSSOVER_METODOS, REINSERCAO_METODOS
from ag_utils import todas_letras
from ag_interface import renderizar_problema_tela
from ag_excel import gerar_relatorio_excel

import sys
import pygame
from itertools import product

sys.stdout.reconfigure(encoding='utf-8')

def mostrar_operacoes(problem, mapping):
    """Exibe as operações e números correspondentes no terminal."""
    all_letters = set("".join("".join(v) for v in problem.values()))
    result = []

    print("\n--- Problema ---")
    for key, value in problem.items():
        mapped_word = "".join(str(mapping.get(letter, "?")) for letter in value)
        print(f"{key}: {''.join(value)} -> {mapped_word}")
        result.append(int(mapped_word))

    if len(result) >= 2:
        soma = sum(result[:-1])
        print(f"Operação: {' + '.join(map(str, result[:-1]))} = {result[-1]}")
        print(f"Resultado calculado: {soma}, Esperado: {result[-1]}")
        print(f"Fitness: {abs(soma - result[-1])}\n")

def executar_configuracao_problema(args):
    """Executa o AG para uma configuração e um problema específico."""
    problem, config = args
    ag = AlgoritmoGenetico(problem, config)
    converg, _, tempo_medio = ag.executar(runs=NUM_EXECUCOES)
    return (config, problem, converg / NUM_EXECUCOES, tempo_medio)

def executar_problema_visualizar(problem, config):
    """Executa o AG e retorna o melhor mapeamento."""
    ag = AlgoritmoGenetico(problem, config)
    _, melhor_individuo, _ = ag.executar(runs=10)  # Execução menor para visualização
    all_letters = todas_letras(problem)
    mapping = {all_letters[i]: melhor_individuo[i] for i in range(len(all_letters))}
    return mapping

def calcular_fitness(mapping, problem):
    """
    Calcula o fitness de um mapeamento para um problema específico.
    O fitness é o valor absoluto da diferença entre a soma das palavras e o resultado esperado.
    :param mapping: Dicionário que mapeia letras para números.
    :param problem: Problema de criptoaritmética (dicionário com palavras).
    :return: Valor do fitness.
    """
    try:
        # Converte as palavras em valores numéricos com base no mapeamento
        valores = []
        for word in problem.values():
            number = int("".join(str(mapping[letter]) for letter in word))
            valores.append(number)
        
        # Calcula o fitness: diferença entre a soma das primeiras palavras e o resultado esperado
        soma = sum(valores[:-1])
        resultado_esperado = valores[-1]
        fitness = abs(soma - resultado_esperado)
        
        return fitness
    except KeyError:
        # Retorna um fitness alto se o mapeamento estiver incompleto
        return float('inf')


def visualizar_problemas_com_interface(problemas, mappings):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Visualização de Problemas - AG Criptoaritimética")
    clock = pygame.time.Clock()
    running = True
    problema_atual = 0

    while running:
        screen.fill((0, 0, 0))
        problem = problemas[problema_atual]
        mapping = mappings[problema_atual]

        # Calcula o fitness
        fitness = calcular_fitness(mapping, problem)

        # Renderiza o problema atual com status do fitness
        renderizar_problema_tela(screen, problem, mapping, y_offset=50, fitness=fitness)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RIGHT and problema_atual < len(problemas) - 1:
                    problema_atual += 1
                elif event.key == pygame.K_LEFT and problema_atual > 0:
                    problema_atual -= 1

        clock.tick(30)
    pygame.quit()


def main():
    print("Executando Algoritmo Genético para todas as configurações...\n")

    # Geração de todas as configurações possíveis
    configuracoes = list(product(TAXAS_MUTACAO, TAXAS_CRUZAMENTO, SELECAO_METODOS, CROSSOVER_METODOS, REINSERCAO_METODOS))
    resultados_etapa1 = []
    solucao_fitness_zero = None  # Para armazenar a solução de fitness 0

    # Etapa 1: Executar AG no primeiro problema para todas as configurações
    print("### Etapa 1: Avaliando configurações no primeiro problema (SEND + MORE = MONEY)")
    with Pool(processes=cpu_count()) as pool:
        args = [(PROBLEMAS[0], config) for config in configuracoes]
        resultados_etapa1 = pool.map(executar_configuracao_problema, args)

    # Selecionar as 4 melhores configurações
    resultados_etapa1.sort(key=lambda x: (-x[2], x[3]))  # Ordena por convergência decrescente e tempo crescente
    melhores_configuracoes = resultados_etapa1[:4]

    print("\n### 4 Melhores Configurações:")
    for i, (config, _, conv, tempo) in enumerate(melhores_configuracoes, 1):
        print(f"{i}. Config: {config}, Convergência: {conv:.2%}, Tempo Médio: {tempo:.4f}s")

    # Verificar e mostrar a solução com fitness 0 no primeiro problema
    print("\n### Solução de Fitness 0 no Problema SEND + MORE = MONEY:")
    for config in configuracoes:
        ag = AlgoritmoGenetico(PROBLEMAS[0], config)
        _, melhor_individuo, _ = ag.executar(runs=1000)  # 1000 execuções conforme especificado
        all_letters = todas_letras(PROBLEMAS[0])
        mapping = {all_letters[i]: melhor_individuo[i] for i in range(len(all_letters))}
        fitness = calcular_fitness(mapping, PROBLEMAS[0])

        if fitness == 0:
            print("\nConfiguração que obteve Fitness 0:")
            print(f"Configuração: {config}")
            mostrar_operacoes(PROBLEMAS[0], mapping)  # Exibe o resultado correto
            solucao_fitness_zero = mapping  # Armazena a solução
            break


    # Caso nenhuma solução com fitness 0 tenha sido encontrada
    if not solucao_fitness_zero:
        print("\nNenhuma solução com Fitness 0 foi encontrada na Etapa 1.")

    # Etapa 2: Executar as 4 melhores configurações em todos os 5 problemas
    print("\n### Etapa 2: Avaliando as melhores configurações em todos os problemas")
    with Pool(processes=cpu_count()) as pool:
        args = [(problem, config) for config, _, _, _ in melhores_configuracoes for problem in PROBLEMAS]
        resultados_etapa2 = pool.map(executar_configuracao_problema, args)

    # Selecionar a melhor configuração global
    melhor_config = max(resultados_etapa2, key=lambda x: x[2])[0]  # Melhor configuração com base na taxa de convergência

    # Visualização de resultados
    print("\n### Visualização das soluções para os problemas:")
    mappings = []
    for problem in PROBLEMAS:
        mapping = executar_problema_visualizar(problem, melhor_config)
        mappings.append(mapping)
        mostrar_operacoes(problem, mapping)

    # Interface gráfica com os resultados
    visualizar_problemas_com_interface(PROBLEMAS, mappings)

    # Geração do relatório Excel
    problema_facil = "SEND + MORE = MONEY"  # Exemplo
    gerar_relatorio_excel(resultados_etapa1, melhores_configuracoes, resultados_etapa2, melhor_config, problema_facil)
    print("\nRelatório Excel gerado com sucesso!")

if __name__ == "__main__":
    main()
