import networkx as nx
import matplotlib.pyplot as plt
from load_data import load_data


def network_graph(dt):
    G = nx.Graph()
    # Extract the necessary columns for the network graph
    parent_child_pairs = dt[['Parent entity (English)', 'Name (English)']].dropna()

    # Add nodes with the 'parent' attribute and set node size based on the number of children
    for parent, children in parent_child_pairs.groupby('Parent entity (English)'):
        G.add_node(parent, type='parent', size=len(children) * 300)  # Size is proportional to the number of children

    # Add child nodes and edges between parent and child nodes
    for _, (parent, child) in parent_child_pairs.iterrows():
        G.add_node(child, type='child', size=100)  # Fixed size for child nodes
        G.add_edge(parent, child)

    # Generate positions for the nodes using the spring layout to spread out the nodes for visibility
    pos = nx.spring_layout(G, k=0.3, iterations=50)

    # Get node sizes from the node attributes
    # node_sizes = [G.nodes[node]['size'] for node in G.nodes()]
    unique_parents = list(set(parent_child_pairs['Parent entity (English)']))
    color_map = plt.cm.get_cmap('hsv', len(unique_parents))
    parent_color_dict = {parent: color_map(i) for i, parent in enumerate(unique_parents)}

    # Assign a color to each node based on the parent
    node_color = []
    node_sizes = []
    for node in G.nodes():
        if G.nodes[node]['type'] == 'parent':
            node_color.append(parent_color_dict[node])
            node_sizes.append(1000)  # Larger size for parent nodes
        else:
            # Find the parent node and assign the same color
            for parent, children in parent_child_pairs.groupby('Parent entity (English)'):
                if node in children['Name (English)'].values:
                    node_color.append(parent_color_dict[parent])
                    break
            node_sizes.append(100)  # Smaller size for child nodes

    # Draw the graph
    plt.figure(figsize=(20, 20))
    nx.draw(G, pos, node_size=node_sizes, node_color=node_color, with_labels=True, font_size=8, edge_color='grey', alpha=0.5)

    # Set plot title and remove axes
    plt.title('Imitated Network Graph with Varied Node Sizes', size=15)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    data = load_data()
    network_graph(data)
