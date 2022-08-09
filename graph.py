import networkx as nx


class Graph:
    def __init__(self, df, src: str, des: str, weight=0):
        self.df = df
        self.G = nx.Graph()
        if weight != 0:
            for index, row in df.iterrows():
                self.G.add_edge(row[src], row[des], weight=row[weight])
        else:
            for index, row in df.iterrows():
                self.G.add_edge(row[src], row[des], weight=0)
