from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt

# Function to generate the subset graph
def generate_subset_graph(elements):
    # Create a directed graph
    graph = nx.DiGraph()
    
    # Sort the elements for consistency
    elements = sorted(elements)
    
    # Generate subsets of all sizes
    for size in range(len(elements), 0, -1):
        subsets = list(combinations(elements, size))
        
        # Map subsets of this size to subsets of size-1
        for subset in subsets:
            graph.add_node(subset)  # Add the subset as a node
            for smaller_subset in combinations(subset, size - 1):
                graph.add_node(smaller_subset)  # Add smaller subset as a node
                graph.add_edge(subset, smaller_subset)  # Add edge from larger to smaller subset

    # Add the empty set as a node
    graph.add_node(())  # Add empty set node
    return graph

# Function to visualize the graph with tweaks
def visualize_graph(graph):
    # Create a layout for the graph
    pos = nx.spring_layout(graph, seed=400)  # Fixed layout for consistency
    plt.figure(figsize=(10, 8))
    
    # Prepare custom labels for nodes
    labels = {}
    for node in graph.nodes():
        if node == ():  # Handle the empty set
            labels[node] = "∅"  # Use the empty set symbol
        else:
            labels[node] = str(node)
    
    # Draw the graph
    nx.draw(graph, pos, with_labels=False, node_size=2000, font_size=10, font_color="white", 
            font_weight="bold", node_color="blue", edge_color="gray")
    
    # Add custom labels
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=10, font_color="white")
    
    plt.title("Subset Graph Visualization", fontsize=14)
    plt.show()
    

# Main script
if __name__ == "__main__":
    elements = [1, 2, 3]  # input elements
    subset_graph = generate_subset_graph(elements)  # Generate the graph
    visualize_graph(subset_graph)  # Visualize the graph
