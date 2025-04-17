from heapq import heapify, heappop, heappush

class Dijkstra:
    def __init__(self, graph: dict = {}):
        self.graph = graph  # A dictionary for the adjacency list

    #detect shortest distances in the graph
    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source value to 0

        # Initialize the predecessors dictionary
        predecessors = {node: None for node in self.graph}

        # Initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()

        while pq:  # While the priority queue isn't empty
            current_distance, current_node = heappop(pq)

            if current_node in visited:
                continue
            visited.add(current_node)

            # Explore neighbors
            for neighbor, weight in self.graph[current_node].items():
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    predecessors[neighbor] = current_node
                    heappush(pq, (tentative_distance, neighbor))

        return distances, predecessors
   
    #return shortest_path + distance
    def shortest_path(self, source: str, target: str):
        # Generate the predecessors dict
        distances, predecessors = self.shortest_distances(source)

        # Check if the target is reachable
        if distances[target] == float("inf"):
            return [], float("inf")  # Return an empty path and infinite distance

        path = []
        current_node = target

        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()
        total_distance = distances[target]
        
        return path, total_distance

    #return shortest_path  for v1
    def shortest_path_v1(self, source: str, target: str):
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)

        path = []
        current_node = target

        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()
        
        return path
