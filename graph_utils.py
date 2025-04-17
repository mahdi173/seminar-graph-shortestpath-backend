import networkx as nx
import my_module
from string import ascii_uppercase
import random
import geojson
from math import radians, sin, cos, sqrt, asin
from collections import defaultdict
import math

class InteractiveGraph:
    def __init__(self, graph: dict = {}):
        self.graph = graph
        self.G = self._create_networkx_graph()

    def generate_random_graph(self, num_nodes, edge_probability, min_weight, max_weight):
        """
            num_nodes: Number of nodes (letters A-Z, up to 26)
            edge_probability: Probability of having an edge between two nodes
            min_weight: Minimum edge weight
            max_weight: Maximum edge weight
        """
        if num_nodes > 26:
            raise ValueError("Maximum 26 nodes supported (A-Z)")
        
        nodes = list(ascii_uppercase[:num_nodes])
        graph = {node: {} for node in nodes}
        
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):  # Avoid self-loops and duplicate edges
                if random.random() < edge_probability:
                    weight = random.randint(min_weight, max_weight)
                    # Undirected graph - add edge in both directions
                    graph[nodes[i]][nodes[j]] = weight
                    graph[nodes[j]][nodes[i]] = weight
                    
        return graph

    def _create_networkx_graph(self):
        G = nx.Graph()
        for node, edges in self.graph.items():
            for neighbor, weight in edges.items():
                G.add_edge(node, neighbor, weight=weight)
        return G

    def shortest_path(self, start, end):
        original_graph = my_module.Graph(self.graph)
        return original_graph.shortest_path(start, end)