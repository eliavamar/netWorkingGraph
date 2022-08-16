from neo4j import GraphDatabase
import nxneo4j as nx
from tqdm import tqdm


class Graph:
    def __init__(self, df, uri: str, user: str, password: str, src: str, des: str, weight=None):
        self.df = df
        self.G = nx.Graph(GraphDatabase.driver(uri=uri, auth=(user, password)))
        self.G.delete_all()
        if weight is not None:
            self.G.relationship_type = weight
        print("Start Build Graph!")
        if weight is not None:

            for i in tqdm(df.index, desc="Loading..."):
                self.G.add_edge(str(df[src][int(i)]), str(df[des][int(i)]), weight=str(df[weight][int(i)]))
        else:
            for i in tqdm(df.index, desc="Loading..."):
                self.G.add_edge(str(df[src][int(i)]), str(df[des][int(i)]), weight=0)
        self.G.edges(data=True)
        print("Finish Build Graph!")

    def draw_graph(self, limit: int):
        nx.draw(self.G, limit)
