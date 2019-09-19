import networkx as nx
import matplotlib.pyplot as plt

def load_graph(name_file):
    G = nx.Graph()
    facilities_nodes = []
    customer_nodes = []
    f = open(name_file)
    # La prima linea contiene due numeri: m facilities, n customers
    first_line = f.readline()
    parameters = []
    for word in first_line.split():
        parameters.append(word)
    # Creazione dei nodi delle facilities e dei clienti
    add_nodes(int(parameters[0]), 'f', G, 0)
    add_nodes(int(parameters[1]), 'd', G, 1)
    # Assegnamento dei costi di installazione delle facilities
    facility_cost = []
    for _ in range(0, int(parameters[0])):
        line = f.readline()
        fixed_cost = line.split()[1]
        facility_cost.append(int(fixed_cost[:-1]))
    i = 0
    for u in G.nodes:
            if G.node[u]['bipartite'] == 0:
                G.node[u]['f'] = facility_cost[i]
                facilities_nodes.append(u)
                i += 1
            else:
                customer_nodes.append(u)
    
    
    # Assegnamento dei costi degli archi
    for u in customer_nodes:
        f.readline()
        i = 0
        while i < int(parameters[0]):
            line = f.readline().split()
            for cost in line:
                G.add_edge('f'+ str(i), u, c = cost)
                i+=1
            
        
    print(len(G.edges))
        
    
    for e in G.edges:
        print(e, " cost:", G.edges[e]['c'])
    f.close()
    return G


def load_demo_graph():

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

def add_nodes(number, prefix, G, b):
    for i in range(0, number):
        if prefix == 'f':
            G.add_node(prefix + str(i), f = 0, bipartite = b)
        else:
            G.add_node(prefix + str(i), bipartite = b)
