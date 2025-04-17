import networkx as nx
import my_module
from string import ascii_uppercase
import random
import geojson
from math import radians, sin, cos, sqrt, asin
from collections import defaultdict
import math
import heapq

class InteractiveGraph:
    def __init__(self, geojson_data):
        self.graph = self.geojson_points_to_graph(geojson_data)
        self.G = self._create_networkx_graph()

    def shortest_path(self, start, end):
        original_graph = my_module.Dijkstra(self.graph)
        return original_graph.shortest_path(start, end)

    def calculate_distance(self, point1, point2):
        R = 6371.0  # Earth's radius in kilometers
        lat1, lon1 = map(math.radians, point1)
        lat2, lon2 = map(math.radians, point2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return round(distance)

    def geojson_points_to_graph(self, geojson_data, k=1):
        """
        Convert GeoJSON data containing Point geometries into a complete graph.
        
        Args:
            geojson_data (dict): GeoJSON data containing Point features.
        
        Returns:
            dict: A graph represented as a dictionary of dictionaries.
        """
        graph = defaultdict(dict)
        node_map = {}  # Maps coordinates to unique node IDs

        # Extract all points from the GeoJSON
        points = []
        for feature in geojson_data.get("features", []):
            geometry = feature.get("geometry", {})
            properties = feature.get("properties", {})
            geom_type = geometry.get("type")
            if geom_type == "Point":
                coords = tuple(geometry.get("coordinates"))
                point_id = properties.get("id")  # Use the 'id' property from GeoJSON
                if point_id is None:
                    raise ValueError("Each GeoJSON feature must have an 'id' property.")
                node_map[coords] = point_id
                points.append(coords)
        
        point_ids = [node_map[point] for point in points]

        # Create edges between all pairs of points
        for i, point1 in enumerate(points):
            distances = []
            for j, point2 in enumerate(points):
                if i != j:
                    distance = self.calculate_distance(point1, point2)
                    distances.append((distance, j))

                # Get the indices of the k nearest neighbors
                nearest_neighbors = [idx for _, idx in heapq.nsmallest(k, distances)]

                for neighbor_idx in nearest_neighbors:
                    point2 = points[neighbor_idx]
                    node1 = node_map[point1]
                    node2 = node_map[point2]
                    distance = self.calculate_distance(point1, point2)
                    graph[node1][node2] = distance
                    graph[node2][node1] = distance  # Undirected graph
        print(dict(graph))
        return dict(graph)

    def get_graph(self):
        return self.graph
