import networkx as nx
import math
class Solution:
    def __init__(self, p, graph):
        self.permutation = p
        self.fitness = 0
        self.G = graph

    def compute_fitness(self):
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
        f = (self.fitness - min_f)/(max_f-min_f)
        alpha = math.e**(-rho*f)
        M = math.floor((alpha*len(self.permutation))-1)
        print(self.fitness, ": ", M)

        

