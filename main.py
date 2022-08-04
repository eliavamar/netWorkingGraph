# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    G = nx.Graph()

    for i in range(20):
        G.add_node(i)
    for i in range(3):
        G.add_edges_from([(i, i+1)], weight=2)
        G.add_edges_from([(i, i * 5)], weight=2)
    elarge = [(u, v) for (u, v, d) in G.edges(data=True)]

    pos = nx.spring_layout(G, seed=50)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G, pos)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, edge_color="b", style="solid")

    # node labels
    nx.draw_networkx_labels(G, pos)
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    plt.axis("off")
    plt.tight_layout()
    plt.show()
