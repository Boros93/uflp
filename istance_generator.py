import networkx as nx
import matplotlib.pyplot as plt

def load_graph(name_file):
    facility_list = ['f0','f1','f2','f3']
    facility_list_cost = [50,30,20,40]
    demand_list = ['d0', 'd1', 'd2']

    transport_cost = 0
    # Creazione Grafo
    G = nx.Graph()
    G.add_nodes_from(facility_list, bipartite=0, y = 0)
    G.add_nodes_from(demand_list, bipartite=1, served=0)
    for f,p in zip(facility_list, facility_list_cost):
        G.add_node(f, f=p)
        for d in demand_list:
            G.add_edge(d, f,  c = transport_cost)
            transport_cost += 1

    return G