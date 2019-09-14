import networkx as nx

class Solution:
    def __init__(self, p, graph):
        self.permutation = p
        self.fitness = 0
        self.G = graph

    def compute_fitness(self):
        # Calcolo costi di istallazione facilities
        i = 0
        for u in self.G.nodes:
            if self.G.node[u]['bipartite'] == 0:
                if(self.permutation[i] == 1): 
                    self.fitness += self.G.node[u]['f']
                i += 1



        

