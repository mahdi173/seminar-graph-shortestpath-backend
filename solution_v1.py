from graph_utils import InteractiveGraph
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

gh ={'Point_1': {'Point_2': 662, 'Point_4': 436, 'Point_5': 316, 'Point_3': 834, 'Point_6': 1251, 'Point_7': 781, 'Point_8': 1187, 'Point_9': 1390, 'Point_10': 2346}, 'Point_2': {'Point_1': 662, 'Point_3': 311, 'Point_7': 173, 'Point_6': 598, 'Point_8': 561, 'Point_10': 1721}, 'Point_4': {'Point_1': 436, 'Point_5': 363, 'Point_9': 974}, 'Point_5': {'Point_1': 316, 'Point_4': 363}, 'Point_3': {'Point_2': 311, 'Point_1': 834, 'Point_6': 481, 'Point_8': 375, 'Point_10': 1515}, 'Point_7': {'Point_2': 173, 'Point_1': 781}, 'Point_6': {'Point_1': 1251, 'Point_2': 598, 'Point_3': 481, 'Point_8': 148, 'Point_10': 1133}, 'Point_8': {'Point_6': 148, 'Point_1': 1187, 'Point_2': 561, 'Point_3': 375}, 'Point_9': {'Point_1': 1390, 'Point_4': 974}, 'Point_10': {'Point_1': 2346, 'Point_2': 1721, 'Point_3': 1515, 'Point_6': 1133}}

interactive_graph = InteractiveGraph(gh)
G = interactive_graph._create_networkx_graph()

selected_nodes = []  # Stores [start, end]
path_edges = []      # Stores edges in the shortest path

fig, ax = plt.subplots(figsize=(12, 10))
pos = nx.spring_layout(G, k=0.5, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=800, node_color='lightblue', ax=ax)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray', ax=ax)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)

# Button to clear selection
clear_ax = plt.axes([0.7, 0.05, 0.2, 0.075])
clear_button = Button(clear_ax, 'Clear Path', color='lightgoldenrodyellow')

def clear_path(event):
   global selected_nodes, path_edges
   selected_nodes = []
   path_edges = []
   redraw_graph()
   plt.title("Click two nodes to find the shortest path", fontsize=10)

clear_button.on_clicked(clear_path)

def on_click(event):
   global selected_nodes, path_edges
   if event.inaxes != ax:
      return
   
   # Find closest node
   dists = {node: (pos[node][0] - event.xdata)**2 + (pos[node][1] - event.ydata)**2 for node in G.nodes}
   closest = min(dists, key=dists.get)
   
   if closest not in selected_nodes:
      selected_nodes.append(closest)
   
   if len(selected_nodes) == 2:
      start, end = selected_nodes
      try:
         path = interactive_graph.shortest_path(start, end)
         path_edges = list(zip(path[:-1], path[1:]))
         redraw_graph()
         plt.title(f"Shortest path: {' → '.join(path)}", fontsize=10)
      except nx.NetworkXNoPath:
         plt.title(f"No path between {start} and {end}", fontsize=10)
         selected_nodes = []

def redraw_graph():
   ax.clear()
   nx.draw_networkx_nodes(G, pos, node_size=800, node_color='lightblue', ax=ax)
   
   # Highlight selected nodes (green = start, red = end)
   if len(selected_nodes) >= 1:
      nx.draw_networkx_nodes(G, pos, nodelist=[selected_nodes[0]], node_size=800, node_color='green', ax=ax)
   if len(selected_nodes) >= 2:
      nx.draw_networkx_nodes(G, pos, nodelist=[selected_nodes[1]], node_size=800, node_color='red', ax=ax)
   
   # Draw all edges
   nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray', ax=ax)
   
   # Highlight shortest path edges
   if path_edges:
      nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='blue', ax=ax)
   
   nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax)
   nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)
   plt.draw()

fig.canvas.mpl_connect('button_press_event', on_click)
plt.title("Click two nodes to find the shortest path", fontsize=10)
plt.axis('off')
plt.tight_layout()
plt.show()
