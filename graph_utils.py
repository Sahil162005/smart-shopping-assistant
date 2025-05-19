import networkx as nx

def parse_delivery_time(delivery_str):
    try:
        parts = delivery_str.replace(" days", "").split("-")
        return sum(map(int, parts)) / len(parts)
    except:
        return 5  # default fallback

def build_graph(products, weight_type='composite'):
    G = nx.Graph()

    for product in products:
        node_id = product['node_id']
        price = product['price']
        delivery = parse_delivery_time(product['delivery_time'])
        rating = product['seller_rating']

        weight = {
            'price': price,
            'delivery': delivery,
            'composite': price + delivery - rating
        }[weight_type]

        G.add_node(node_id, **product, weight=weight)

    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            p1, p2 = products[i], products[j]
            id1, id2 = p1['node_id'], p2['node_id']
            w = abs(p1['price'] - p2['price']) + abs(
                parse_delivery_time(p1['delivery_time']) - parse_delivery_time(p2['delivery_time'])
            )
            G.add_edge(id1, id2, weight=w)

    return G
