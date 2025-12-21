import networkx as nx
import matplotlib.pyplot as plt

def draw_heap(heap):
    G = nx.DiGraph()
    pos = {}

    def add_edges(i, x=0, y=0, layer=1):
        if i >= len(heap):
            return
        G.add_node(i, label=heap[i])
        pos[i] = (x, -y)

        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(heap):
            G.add_edge(i, left)
            add_edges(left, x - 1 / (2**layer), y + 1, layer + 1)
        if right < len(heap):
            G.add_edge(i, right)
            add_edges(right, x + 1 / (2**layer), y + 1, layer + 1)

    add_edges(0)

    labels = nx.get_node_attributes(G, 'label')
    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=2000, node_color="skyblue", arrows=False)
    plt.show()

heap = [10, 5, 3, 2, 4, 1]
draw_heap(heap)