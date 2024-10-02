import networkx as nx

class SoftwareDNA:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id, node_type, properties=None):
        self.graph.add_node(node_id, type=node_type, properties=properties or {})

    def add_edge(self, source_id, target_id, edge_type):
        self.graph.add_edge(source_id, target_id, type=edge_type)

    def get_node(self, node_id):
        return self.graph.nodes[node_id]

    def get_edges(self, node_id):
        return self.graph.edges(node_id, data=True)  

    def node_count(self):
        return self.graph.number_of_nodes()

    def edge_count(self):
        return self.graph.number_of_edges()