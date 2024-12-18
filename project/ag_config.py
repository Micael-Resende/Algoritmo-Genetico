# ag_config.py
import pygame

# Inicialização do pygame
pygame.init()

# Dimensões da janela
LARGURA = 800
ALTURA = 600

# Configurações das fontes
FONT_SIZE = 24                # Tamanho da fonte padrão
TITLE_FONT_SIZE = 32          # Tamanho da fonte de título
SMALL_FONT_SIZE = 18          # Tamanho da fonte pequena

# Fontes
FONT = pygame.font.Font(None, FONT_SIZE)           # Fonte padrão
TITLE_FONT = pygame.font.Font(None, TITLE_FONT_SIZE)  # Fonte para títulos
SMALL_FONT = pygame.font.Font(None, SMALL_FONT_SIZE)  # Fonte pequena

# Configurações do Algoritmo Genético
POP_SIZE = 100               # Tamanho da população
GENERATIONS = 50             # Número de gerações
CACHE_SIZE = 100000          # Tamanho máximo do cache de fitness
NUM_EXECUCOES = 1000         # Número de execuções por problema
LIMIT_NO_IMPROVE = 20        # Limite de gerações sem melhoria antes do algoritmo parar

# Taxas e métodos do AG
TAXAS_MUTACAO = [0.05, 0.1]
TAXAS_CRUZAMENTO = [0.6, 0.8]
SELECAO_METODOS = ["Roleta", "Torneio"]
CROSSOVER_METODOS = ["Ciclico", "PMX"]
REINSERCAO_METODOS = ["Ordenada", "Elitismo"]
