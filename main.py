from immune_algorithm import main_loop
# Parametri
generation = 10
population = 10 # d
clonation = 2 # dup
rho = 1
tau_b = 5
length_sol = 5 # Calcolare la lunghezza della soluzione dal numero delle facilities

main_loop(generation, population, clonation, length_sol)
