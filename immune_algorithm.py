from solution import Solution
import random 
import copy
import math 

def main_loop(graph, generation, d, dup, rho, tau_b, l):
    population = initialize_population(d, tau_b, l, graph)
    compute_fitness(population)
    best_solution = choose_best_solution(population)
    worst_solution = choose_worst_solution(population) 
    print("Best Solution:", best_solution.permutation, " with fitness:", best_solution.fitness)
    print("Worst Solution:", worst_solution.permutation, " with fitness:", worst_solution.fitness)
    # Inizio Ciclo generazioni
    for _ in range(0,generation):
        # --- Cloning ---
        population_clo = clonation_operator(population, dup, tau_b, graph)
        # --- Hypermutation ---
        hypermutation_operator(population_clo, rho, worst_solution, best_solution)
        compute_fitness(population_clo)
        # Concatenazione vecchia popolazione con quella ipermutata
        population = population + population_clo
        # --- Aging ---
        best_solution = choose_best_solution(population)
        print("Best Solution:", best_solution.permutation, " with fitness:", best_solution.fitness, "and age:", best_solution.age)
        population = aging_operator(population, tau_b, best_solution)
        print("--- Fine generazione ---")

        # mu-lambda selection (Da implementare)
        new_population = []
        for _ in range(0, d):
            new_population.append(random.choice(population))
        population = new_population

# Inizializzazione random di una popolazione di grandezza d e ogni soluzione lunga l
def initialize_population(population_number, tau_b, l, G):
    population = []
    for _ in range(0, population_number):
        new_cell = gen_solution(l, tau_b, G)
        # Se genera soluzioni con tutti 0, rigenera la soluzione
        while(all(c == 0 for c in new_cell.permutation)):
            new_cell = gen_solution(l, tau_b, G)
        population.append(new_cell)
    print("+++ Inizializzazione popolazione conclusa +++")
    return population

# Genera una soluzione random con una distribuzione uniforme
def gen_solution(l, tau_b, G):
    permutation = []
    for _ in range(0,l):
        r = random.uniform(0,1)
        if r >= 0.5:
            permutation.append(1)
        else:
            permutation.append(0)
    upper_bound = math.floor((2/3)*tau_b)
    age = random.randint(0,upper_bound)
    result = Solution(permutation, 0, age, G)
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

# --- OPERATORI ---
# Clonazione dup volte
def clonation_operator(population, dup, tau_b, G):
    population_clo = []
    for cell in population:
        for _ in range(0,dup):
            upper_bound = math.floor((2/3)*tau_b)
            age = random.randint(0,upper_bound)
            population_clo.append(Solution(cell.permutation, cell.fitness, age, G))
    print ("*** Clonazione terminata ***")
    return population_clo

def hypermutation_operator(population, rho, max_f, min_f):
    for cell in population:
        cell.hypermutation(rho, max_f.fitness, min_f.fitness - (min_f.fitness*50/100))
    print('<<< Hypermutazione terminata >>>')

def aging_operator(population, tau_b, best_solution):
    for p in population:
        if p.age > (tau_b + 1):
            if p != best_solution:
                population.remove(p)
            else:
                print("Soluzione migliore non cancellata:", p.permutation, p.fitness)
        else:
            p.age += 1

    return population