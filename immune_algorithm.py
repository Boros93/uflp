from solution import Solution
import random 


def compute_fitness(population):
    for p in population:
        p.compute_fitness()

def main_loop(graph, generation, d, dup, l):
    population = initialize_population(d, l, graph)
    print(population[0].fitness)
    print(population[0].permutation)
    compute_fitness(population)
    print(population[0].fitness)

# Inizializzaione random di una popolazione di grandezza d e ogni soluzione lunga l
def initialize_population(population_number, l, G):
    population = []
    for _ in range(0, population_number):
        population.append(gen_solution(l, G))
    print("--- Inizializzazione popolazione conclusa ---")
    return population

# Genera una soluzione random con una distribuzione uniforme
def gen_solution(l, G):
    permutation = []
    for _ in range(0,l):
        r = random.uniform(0,1)
        if r >= 0.5:
            permutation.append(1)
        else:
            permutation.append(0)
    result = Solution(permutation, G)
    return result





