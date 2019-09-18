import networkx as nx
import math
import random
class Solution:
    def __init__(self, p, f, tau_b, graph):
        self.permutation = p
        self.fitness = f
        self.G = graph
        self.age = tau_b

    def compute_fitness(self):
        self.fitness = 0
        demand_nodes = list()
        # Calcolo costi di istallazione facilities
        i = 0
        for u in self.G.nodes:
            if self.G.node[u]['bipartite'] == 0:
                if(self.permutation[i] == 1): 
                    self.fitness += self.G.node[u]['f']
                    self.G.node[u]['y'] = 1
                i += 1
            else:
                demand_nodes.append(u)
        
        # Allocation
        edges_cost = nx.get_edge_attributes(self.G, 'c')
        facility = nx.get_node_attributes(self.G, 'y')

        for d in demand_nodes:
            min_cost = 10000
            for uv in self.G.edges(d):
                # Aggiungere condizione se f = 1
                if edges_cost[uv[::-1]] < min_cost and facility[uv[1]]:
                    min_cost = edges_cost[uv[::-1]]
            self.fitness += min_cost

    def hypermutation(self, rho, max_f, min_f):
        l = len(self.permutation)
        # Calcolo del numero delle mutazioni M
        f = 1 - (self.fitness - min_f)/(max_f-min_f)
        alpha = math.e**(-rho*f)
        M = math.floor((alpha*l)-1)
        # Mutazioni
        position = random.sample(range(0, l), M)
        self.swap(position)
        # Se trasforma la soluzione in una soluzione non valida, rifare la mutazione
        while(self.check_validity()):
            self.swap(position)


    def swap(self, position):
        new_solution = list(self.permutation)
        for pos in position:
            new_solution[pos] = int(not new_solution[pos])
        self.permutation = new_solution
        
    def check_validity(self):
        if all(c == 0 for c in self.permutation):
            return True
        else:
            return False
        

