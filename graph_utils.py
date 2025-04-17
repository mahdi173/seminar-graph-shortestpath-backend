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
   
    #create graph
    def _create_networkx_graph(self):
        G = nx.Graph()
        for node, edges in self.graph.items():
            for neighbor, weight in edges.items():
                G.add_edge(node, neighbor, weight=weight)
        return G
        
    # return short distance by Dijkstra
    def shortest_path(self, start, end):
        original_graph = my_module.Dijkstra(self.graph)
        return original_graph.shortest_path_v1(start, end)