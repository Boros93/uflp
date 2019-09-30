from immune_algorithm import main_loop
from istance_generator import load_graph
import statistics 
# Parametri
generation = 3000
population = 100# d
clonation = 2 # dup
mutation_rate = 0.5
tau_b = 100

graph, length_sol = load_graph('Instances/cap131.txt')

result = []
for i in range(0, 20):
    result.append(main_loop(graph, generation, population, clonation, mutation_rate, tau_b, length_sol))
print("Results:", result)
print("Mean:", statistics.mean(result))
print("Best:", min(result))
print("Worst:", max(result))
print("Std:", statistics.stdev(result))