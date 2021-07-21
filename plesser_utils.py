import math
import copy
import networkx as nx
import matplotlib.pyplot as plt

def get_pairs(array):
    permutations = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            lo = min(array[i], array[j])
            hi = max(array[i], array[j])
            permutations.append((lo, hi))
    return permutations

def reverse_destination_order(destinations):
    new_destinations = destinations.copy()
    new_destinations[1] = destinations[2]
    new_destinations[2] = destinations[1]
    return new_destinations

def draw_graph(nodes, edges):
    graph = nx.Graph()

    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    colormap = list(map(lambda x: { 'e': 'white', 'w': '#dddddd', 'b': '#989AC1' }[x[0]], nodes))

    fixed_positions = {}
    for node in graph:
        if node[0] == 'e':
            angle = 2 * math.pi / 8 * (8 - int(node[1])) - 2.7
            x = math.cos(angle)
            y = math.sin(angle)
            fixed_positions[node] = (x, y)

    pos = nx.spring_layout(graph, k=0.13, pos=fixed_positions, fixed=fixed_positions.keys(), threshold=0.0000001)

    plt.figure(figsize=(7, 7))
    nx.draw_networkx(graph, pos=pos, node_color=colormap, node_size=500, width=3, edge_color='#aaa')
    plt.show()

def draw_node_edges(node_edges):
    nodes = []
    edges = []
    for node, destinations in node_edges:
        if node not in nodes:
            nodes.append(node)
        for destination in destinations:
            if destination not in nodes:
                nodes.append(destination)
            if (destination, node) not in edges:
                edges.append((node, destination))            
    draw_graph(nodes, edges)