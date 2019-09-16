from solution import Solution
import random 
import copy
import math 

def main_loop(graph, generation, d, dup, rho, l):
    population = initialize_population(d, l, graph)
    compute_fitness(population)
    for cell in population:
        print(cell.permutation)
        print(cell.fitness)
    best_solution = choose_best_solution(population)
    worst_solution = choose_worst_solution(population) 
    print("Best Solution:", best_solution.permutation, " with fitness:", best_solution.fitness)
    print("Worst Solution:", worst_solution.permutation, " with fitness:", worst_solution.fitness)
    # Inizio Ciclo generazioni
    for _ in range(0,generation):
        # --- Cloning ---
        #population_clo = clonation(population, dup)
        # --- Hypermutation ---
        population_hyp = hypermutation(population, rho, worst_solution, best_solution)


# Inizializzazione random di una popolazione di grandezza d e ogni soluzione lunga l
def initialize_population(population_number, l, G):
    population = []
    for _ in range(0, population_number):
        new_cell = gen_solution(l, G)
        # Se genera soluzioni con tutti 0, rigenera la soluzione
        while(all(c == 0 for c in new_cell.permutation)):
            new_cell = gen_solution(l, G)
        population.append(new_cell)
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

def choose_best_solution(population):
    min_sol = math.inf
    for cell in population:
        if cell.fitness < min_sol:
            best_solution = cell
            min_sol = cell.fitness
    return best_solution

def choose_worst_solution(population):
    max_sol = 0
    for cell in population:
        if cell.fitness > max_sol:
            worst_solution = cell
            max_sol = cell.fitness
    return worst_solution

# Calcolo della fitness per ogni B cell
def compute_fitness(population):
    for p in population:
        p.compute_fitness()

# Clonazione dup volte
def clonation(population, dup):
    population_clo = []
    for cell in population:
        for _ in range(0,dup):
            population_clo.append(copy.copy(cell))
    print ("--- Clonazione terminata ---")
    return population_clo

def hypermutation(population, rho, max_f, min_f):
    population_hyp = []
    for cell in population:
        print(cell.hypermutation(rho, max_f.fitness, min_f.fitness - (min_f.fitness*50/100)))
    return 0



