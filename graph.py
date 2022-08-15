from neo4j import GraphDatabase
import nxneo4j as nx


class Graph:
    def __init__(self, df, uri: str, user: str, password: str, src: str, des: str, weight=0):
        self.df = df
        self.G = nx.Graph(GraphDatabase.driver(uri=uri, auth=(user, password)))
        self.G.delete_all()
        if weight != 0:
            self.G.relationship_type = weight
        print("Start Build Graph!")
        if weight != 0:
            for i in range(1, len(df) + 1):
                self.G.add_edge(str(df[src][i]), str(df[des][i]), weight=str(df[weight][i]))
        else:
            for i in range(1, len(df) + 1):
                self.G.add_edge(str(df[src][i]), str(df[des][i]), weight=0)
                print(i)
        self.G.edges(data=True)
        print("Finish Build Graph!")

    def draw_graph(self, limit: int):
        nx.draw(self.G, limit)
