from immune_algorithm import main_loop
from istance_generator import load_graph
# Parametri
generation = 1
population = 5 # d
clonation = 5 # dup
mutation_rate = 0.5
tau_b = 5
length_sol = 4 # Calcolare la lunghezza della soluzione dal numero delle facilities
graph = load_graph('cap71.txt')

main_loop(graph, generation, population, clonation, mutation_rate, length_sol)
