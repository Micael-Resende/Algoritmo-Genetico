from ag_utils import fitness_com_cache
from ag_config import POP_SIZE, GENERATIONS, CACHE_SIZE, LIMIT_NO_IMPROVE
import random
import time

class AlgoritmoGenetico:
    def __init__(self, problem, config=None):
        """
        Inicializa o algoritmo genético.
        :param problem: O problema de criptoaritmética.
        :param config: Configuração específica do AG (taxas e métodos).
        """
        self.problem = problem
        self.config = config or (0.05, 0.6, "Roleta", "Ciclico", "Ordenada")  # Default

        # Desempacotando a configuração
        self.tm, self.tc, self.selecao, self.crossover, self.reinsercao = self.config

    def criar_individuo(self):
        """Cria um indivíduo como uma permutação dos dígitos 0 a 9."""
        return random.sample(range(10), 10)

    def mutacao_swap(self, ind):
        """Realiza uma única troca de dois elementos em um indivíduo."""
        a, b = random.sample(range(10), 2)
        ind[a], ind[b] = ind[b], ind[a]
        

    # Técnica de recombinação, que envolve permutações(arranjo ou organização) com conjunto de  letras que precisam ser associadas a números.
    def crossover_pmx(self, p1, p2):
        """Realiza o crossover PMX(Partially Matched Crossover) entre dois pais."""
        size = len(p1)
        child = [None] * size
        idx1, idx2 = sorted(random.sample(range(size), 2))

        # Copia o segmento do pai 1
        child[idx1:idx2] = p1[idx1:idx2]
        mapping = {p1[i]: p2[i] for i in range(idx1, idx2)}

        # Preenche os valores restantes
        for i in range(size):
            if child[i] is None:
                val = p2[i]
                while val in mapping:
                    val = mapping[val]
                child[i] = val
        return child

    def selecionar_pais(self, pop):
        """Seleciona dois pais com base no método especificado."""
        if self.selecao == "Roleta":
            return random.choices([ind for ind, _ in pop], weights=[1 / (f + 1) for _, f in pop], k=2)
        elif self.selecao == "Torneio":
            return [min(random.sample(pop, 3), key=lambda x: x[1])[0] for _ in range(2)]
        return random.sample([ind for ind, _ in pop], 2)

    def reinserir_populacao(self, nova_populacao, pop):
        """Reinsere a nova população com base no método especificado."""
        if self.reinsercao == "Ordenada":
            nova_populacao.sort(key=lambda x: x[1])
            return nova_populacao[:POP_SIZE]
        elif self.reinsercao == "Elitismo":
            elite = pop[:POP_SIZE // 5]  # 20% de elitismo
            nova_populacao.extend(elite)
            nova_populacao.sort(key=lambda x: x[1])
            return nova_populacao[:POP_SIZE]
        return nova_populacao

    def inicializar_populacao(self):
        """Inicializa a população, garantindo que não haja duplicatas."""
        pop = set()
        while len(pop) < POP_SIZE:
            individuo = tuple(self.criar_individuo())
            pop.add(individuo)
        return [(list(ind), float('inf')) for ind in pop]

    def executar(self, runs=1):
        """
        Executa o algoritmo genético.
        Retorna o número de convergências, o melhor indivíduo e o tempo médio de execução.
        """
        converg = 0
        melhor_individuo = None
        tempo_inicial = time.time()

        for _ in range(runs):
            pop = self.inicializar_populacao()
            melhor = float('inf')
            sem_melhora = 0

            for geracao in range(GENERATIONS):
                # Avaliação da população
                pop = [(ind, fitness_com_cache(ind, self.problem, CACHE_SIZE)) for ind, _ in pop]
                pop.sort(key=lambda x: x[1])  # Ordena pelo menor fitness

                # Atualiza o melhor indivíduo
                if pop[0][1] < melhor:
                    melhor = pop[0][1]
                    melhor_individuo = pop[0][0]
                    sem_melhora = 0
                else:
                    sem_melhora += 1

                # Critério de parada
                if melhor == 0 or sem_melhora >= LIMIT_NO_IMPROVE:
                    converg += 1
                    break

                # Geração da próxima população
                nova_populacao = []
                while len(nova_populacao) < POP_SIZE:
                    p1, p2 = self.selecionar_pais(pop)
                    if self.reinsercao == "Elitismo":
                        taxa_cruzamento = 0.8
                    else:
                        taxa_cruzamento = self.tc

                    if random.random() < taxa_cruzamento:
                        filho = self.crossover_pmx(p1, p2)
                    else:
                        filho = p1[:]
                    if random.random() < self.tm:
                        self.mutacao_swap(filho)
                    nova_populacao.append((filho, float('inf')))

                # Reinserção
                pop = self.reinserir_populacao(nova_populacao, pop)

            # Se encontrou solução perfeita, encerra
            if melhor == 0:
                break

        tempo_total = time.time() - tempo_inicial
        return converg, melhor_individuo, tempo_total / runs
