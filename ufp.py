import networkx as nx
import matplotlib.pyplot as plt

# Passando un vettore di y, costruire il grafo allocato
def build_graph(G, solution):
    R = nx.Graph()
    # --- Assegnazione del vettore Y ---
    # Divido gli insieme di nodi
    facility_nodes = list()
    demand_nodes = list()
    for u in G.nodes:
        if G.node[u]['bipartite'] == 0:
                facility_nodes.append(u)
        else:
                demand_nodes.append(u)
    # Attivo le rispettive facility
    i = 0
    for y in solution:
        G.node[facility_nodes[i]]['y'] = y
        i += 1
    
    # --- ALLOCATION ---
    edges = nx.get_edge_attributes(G, 'c')
    for d in demand_nodes:
        min_cost = 10000
        edge_min = 0
        for uv in G.edges(d):
                # Aggiungere condizione se f = 1
                if edges[uv[::-1]] < min_cost:
                        min_cost = edges[uv[::-1]]
                        edge_min = uv
        print(edge_min)
        R.add_edge(edge_min[0], edge_min[1])
    return R
    




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

plt.subplot(121)
R = build_graph(G,[1,1,0,1])

left = nx.bipartite.sets(G)[0]
pos = nx.bipartite_layout(G, left)
edges = nx.get_edge_attributes(G, 'c')
nx.draw(G, with_labels=True, font_weight='bold', pos=pos)
nx.draw_networkx_edge_labels(G,font_weight='bold', edge_labels=edges, pos = pos)
# nx.draw(R, with_labels=True, font_weight='bold')
plt.show()