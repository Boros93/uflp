from immune_algorithm import main_loop
from istance_generator import load_graph
# Parametri
generation = 200
population = 100 # d
clonation = 4 # dup
mutation_rate = 0.7
tau_b = 10 # Calcolare la lunghezza della soluzione dal numero delle facilities
graph, length_sol = load_graph('Instances/cap71.txt')


main_loop(graph, generation, population, clonation, mutation_rate, tau_b, length_sol)
