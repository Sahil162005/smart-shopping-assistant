🛒 Smart Shopping Assistant
A graph-based recommendation system to help users find the best product option across multiple platforms (e.g., Amazon, Flipkart) based on price, delivery time, and seller rating.

🚀 Features
📦 Converts product listings into a graph

🔗 Nodes represent products from different platforms

🧮 Edges represent weighted differences (price, delivery time)

🧠 Uses Dijkstra’s algorithm to find:

Cheapest deal

Fastest delivery

Best overall option (composite score)

📊 Outputs path and total score

🧰 Built using Python and NetworkX
├── dijkstra_runner.py              # Main script to run graph search
├── graph_utils.py                  # Builds the product graph
├── product_data_with_nodeid.json   # Dataset (preprocessed products)
├── results.json                    # Output (optimal path info)

⚙️ Technologies Used
Python 🐍

NetworkX 🔗

JSON 🧾
💡 How It Works
Load product data from a JSON file

Build a graph:

Nodes = products

Edges = differences in price and delivery

Apply Dijkstra’s algorithm from the selected product

Return the best option across all platforms
