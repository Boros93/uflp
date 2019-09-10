from solution import Solution
import random 


def compute_fitness(population):
    return 1

def main_loop(generation, d, dup, l):
    population = initialize_population(d, l)
    #population = compute_fitness(population)
    for solution in population:
        print(solution.p)

# Inizializzaione random di una popolazione di grandezza d e ogni soluzione lunga l
def initialize_population(population_number,l):
    population = []
    for _ in range(0, population_number):
        population.append(gen_solution(l))
    print("--- Inizializzazione popolazione conclusa ---")
    return population

# Genera una soluzione random con una distribuzione uniforme
def gen_solution(l):
    permutation = []
    for _ in range(0,l):
        r = random.uniform(0,1)
        if r >= 0.5:
            permutation.append(1)
        else:
            permutation.append(0)
    result = Solution(permutation)
    return result





