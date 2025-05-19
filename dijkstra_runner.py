import json
import networkx as nx
from graph_utils import build_graph

# Loading all products from the JSON file
with open("product_data_with_nodeid.json") as f:
    products = json.load(f)
start_node = "Amazon_Amazon_Laptop_Model_1"
print(f" Start node: {start_node}")
print(f" Total products loaded: {len(products)}")

G = build_graph(products, weight_type='composite')
print(f" Total nodes in graph: {len(G.nodes)}")

# Check if start_node exists in the graph
if start_node not in G:
    print(f" Start node '{start_node}' not found in graph nodes!")
    exit(1)

def find_best_path(graph, start_node):
    try:
        # Computing the  shortest paths from start_node to all reachable nodes
        lengths, paths = nx.single_source_dijkstra(graph, start_node, weight='weight')
    except Exception as e:
        print(f"Error computing paths: {e}")
        return None, None

    best_score = float('inf')
    best_path = None

    for target_node, dist in lengths.items():
        if target_node == start_node:
            continue
        if dist < best_score:
            best_score = dist
            best_path = paths[target_node]

    return best_path, best_score

# Finding the best part
path, score = find_best_path(G, start_node)

# Printing the result
if path:
    print(f"\nBest Path from {start_node}:")
    for node in path:
        product = G.nodes[node]
        print(f" {product['platform']} | {product['product_name']} | ₹{product['price']} | {product['delivery_time']}")
    print(f"\nTotal Composite Score: {score}")
else:
    print("No path found from the selected product.")
