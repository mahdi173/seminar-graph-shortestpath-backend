from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from graph_utils_v2 import InteractiveGraph

app = Flask(__name__)
CORS(app)

@app.route('/calculate_path', methods=['POST'])
def calculate_path():
    try:
        # Get the data from the request
        data = request.get_json()
        geojson_data = data['geojson']
        departure = data['departure']
        arrival = data['arrival']
        interactive_graph = InteractiveGraph(geojson_data)
        path, total_distance  = interactive_graph.shortest_path(departure, arrival)

        return jsonify({
            "path": path,
            "total_distance": total_distance
        }), 200
    except Exception as e:
        # Handle errors
        print("Error processing GeoJSON:", str(e))
        return jsonify({"error": "Failed to process GeoJSON"}), 500

@app.route('/get_graph', methods=['POST'])
def get_graph():
    try:
        # Parse the incoming JSON payload
        data = request.get_json()
        geojson_data = data['geojson']

        # Convert GeoJSON data to a graph
        interactive_graph =  InteractiveGraph(geojson_data)
        graph_dict = interactive_graph.get_graph()
        # Return the graph as JSON
        return jsonify({
            "nodes": list(graph_dict.keys()),
            "edges": [
                {"source": source, "target": target, "distance": distance}
                for source, neighbors in graph_dict.items()
                for target, distance in neighbors.items()
            ]
        }), 200
    except Exception as e:
        print("Error processing request:", str(e))
        return jsonify({"error": "Failed to generate the graph"}), 500
        
if __name__ == '__main__':
    app.run(debug=True)