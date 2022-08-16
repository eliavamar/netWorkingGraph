from neo4j import GraphDatabase
import nxneo4j as nx

from custom_csv import Csv
from graph import Graph
from gui import gui

if __name__ == '__main__':
    gui()
    # neo4j example for custom graph
    # csv = Csv("./x_test.csv")
    # G = Graph(csv.get_df(), "bolt://3.82.246.160:7687", "neo4j", "raises-fiction-voids", "src_ip", "dst_ip")
    # G.draw_graph(len(csv.get_df()))

    # neo4j example
    # uri = "bolt://3.82.246.160:7687"
    # # custom URL for Sandbox or Aura
    # user = "neo4j"
    # password = "raises-fiction-voids"
    # driver = GraphDatabase.driver(uri=uri, auth=(user, password))
    # G = nx.Graph(driver)
    # G.relationship_type = "Weight"
    # G.delete_all()
    # G.add_node(1)  # single node
    # G.add_nodes_from([2, 3, 4])  # multiple nodes
    # G.add_edge(1, 2, weight=3)  # single edge
    # G.add_edges_from([(2, 3), (3, 4)])
    # G.add_node('Mike', gender='M', age=17)
    # G.add_edge('Mike', 'Jenny')
    # print(list(G.edges(data=True)))
    # nx.draw(G)
    # end example

    # example how to build graph from cvs file (make sure that you use "from graph import Graph" and not from nx)
    # csv = Csv("./conn250K.csv")
    # input_arr = csv.get_arr_for_predict_by_columns(["src_bytes", "dst_bytes"])
    # print(input_arr)
    # G = Graph(csv.get_df(), "src_bytes", "dst_bytes")
    # res_arr = isolation_forest(input_arr) # we can use dbscan as wall
    # csv.result_to_csv(res_arr)
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
