from algorithms import dbscan, isolation_forest
from custom_csv import Csv
from graph import Graph

if __name__ == '__main__':
    # example how to build graph from cvs file (make sure that you use "from graph import Graph" and not from nx)
    csv = Csv("./conn250K.csv")
    input_arr = csv.get_arr_for_predict_by_columns(["src_bytes", "dst_bytes"])
    print(input_arr)
    G = Graph(csv.get_df(), "src_bytes", "dst_bytes")
    res_arr = isolation_forest(input_arr) # we can use dbscan as wall
    csv.result_to_csv(res_arr)
    # end example


    # example how to build and draw regular graph
    # numpy.savetxt("test.csv", arr,  delimiter=",", format='%10.0f')
    #
    # G = nx.Graph()
    #
    # for i in range(20):
    #     G.add_node(i)
    # for i in range(3):
    #     G.add_edges_from([(i, i+1)], weight=2)
    #     G.add_edges_from([(i, i * 5)], weight=2)
    # elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
    #
    # pos = nx.spring_layout(G, seed=50)  # positions for all nodes - seed for reproducibility
    #
    # # nodes
    # nx.draw_networkx_nodes(G, pos)
    #
    # # edges
    # nx.draw_networkx_edges(G, pos, edgelist=elarge, edge_color="b", style="solid")
    #
    # # node labels
    # nx.draw_networkx_labels(G, pos)
    # # edge weight labels
    # edge_labels = nx.get_edge_attributes(G, "weight")
    # nx.draw_networkx_edge_labels(G, pos, edge_labels)
    #
    # plt.axis("off")
    # plt.tight_layout()
    # plt.show()
