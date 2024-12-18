# ag_utils.py
from collections import OrderedDict
import math

fitness_cache = OrderedDict()

def todas_letras(problem):
    return list(set("".join("".join(v) for v in problem.values())))

def fitness(individuo, problem):
    all_letters = todas_letras(problem)
    mapping = {all_letters[i]: individuo[i] for i in range(len(all_letters))}
    try:
        values = [int("".join(str(mapping[c]) for c in word)) for word in problem.values()]
        return abs(sum(values[:-1]) - values[-1])
    except ValueError:
        return math.inf

def fitness_com_cache(individuo, problem, cache_size):
    key = tuple(individuo)
    if key not in fitness_cache:
        all_letters = todas_letras(problem)
        mapping = {all_letters[i]: individuo[i] for i in range(len(all_letters))}
        fitness_cache[key] = calcular_fitness(mapping, problem)
        if len(fitness_cache) > cache_size:
            fitness_cache.popitem(last=False)  # Remove o mais antigo
    return fitness_cache[key]

# def calcular_fitness(mapping, problem):
#     """
#     Calcula o fitness do indivíduo.
#     Retorna o erro absoluto entre a soma das palavras de entrada e a palavra resultado.
#     """
#     try:
#         words = list(problem.values())
#         mapped_values = []
#         for word in words:
#             number = "".join(str(mapping[letter]) for letter in word)
#             if number[0] == '0':  # Impede números com zero na posição inicial
#                 return float('inf')
#             mapped_values.append(int(number))
        
#         soma = sum(mapped_values[:-1])
#         resultado = mapped_values[-1]
#         return abs(soma - resultado)
#     except (KeyError, ValueError):
#         return float('inf')

def calcular_fitness(mapping, problem):
    """
    Calcula o fitness do indivíduo.
    Retorna o erro absoluto entre a soma das palavras de entrada e a palavra resultado.
    """
    try:
        words = list(problem.values())
        mapped_values = []
        for word in words:
            number = "".join(str(mapping[letter]) for letter in word)
            if number[0] == '0':  # Impede números com zero na posição inicial
                return float('inf')
            mapped_values.append(int(number))
        
        soma = sum(mapped_values[:-1])
        resultado = mapped_values[-1]
        return abs(soma - resultado)  # Fitness = erro absoluto
    except (KeyError, ValueError):
        return float('inf')























# def calcular_fitness(mapping, problem):
#     """
#     Calcula o fitness do indivíduo.
#     Retorna o erro absoluto entre a soma das palavras de entrada e a palavra resultado.
#     Penaliza mapeamentos com zeros em posições iniciais ou incompletos.
#     """
#     try:
#         words = list(problem.values())  # Palavras do problema
#         mapped_values = []

#         # Converte cada palavra em número usando o mapeamento
#         for word in words:
#             number = "".join(str(mapping.get(letter, "?")) for letter in word)

#             # Verificação de valores inválidos ou incompletos
#             if "?" in number or number[0] == '0':
#                 return float('inf')  # Penaliza números inválidos ou incompletos

#             mapped_values.append(int(number))  # Converte a palavra mapeada em número

#         # Calcula a soma das palavras de entrada e o valor esperado
#         soma = sum(mapped_values[:-1])  # Soma das palavras de entrada
#         resultado = mapped_values[-1]   # Palavra de resultado
#         fitness = abs(soma - resultado)  # Fitness = diferença absoluta

#         return fitness
#     except (KeyError, ValueError):
#         # Retorna fitness alto se ocorrer erro no mapeamento ou conversão
#         return float('inf')
