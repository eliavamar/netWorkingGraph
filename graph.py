import pandas as pd
import networkx as nx


class Graph:
    def __init__(self, df, src: str, des: str, weight: str):
        self.df = df
        self.G = nx.Graph()
        for row in df.rows:
            self.G.add_edge(row[src], row[des], weight=row[weight])

