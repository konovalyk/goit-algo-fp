import uuid
import math
from typing import List, Optional
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import cm, colors as mpl_colors


class Node:
    def __init__(self, key, color: str = "skyblue"):
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph: nx.DiGraph, node: Optional[Node], pos: dict, x=0.0, y=0.0, layer=1) -> nx.DiGraph:
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / (2 ** layer)
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / (2 ** layer)
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node, title: str = "Бінарне дерево") -> None:
    tree = nx.DiGraph()
    pos = {tree_root.id: (0.0, 0.0)}
    add_edges(tree, tree_root, pos)

    node_colors = [data["color"] for _, data in tree.nodes(data=True)]
    labels = {node_id: data["label"] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(9, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=node_colors)
    plt.axis("off")
    plt.show()


def _depth_color(index: int, max_index: int) -> str:
    if max_index < 0:
        return "#87ceeb"
    max_depth = int(math.log2(max_index + 1))
    depth = int(math.log2(index + 1)) if index >= 0 else 0
    t = depth / max(1, max_depth)
    rgba = cm.Reds(0.3 + 0.7 * t) 
    return mpl_colors.to_hex(rgba)


def heap_to_tree(heap: List[int], use_depth_colors: bool = True) -> Optional[Node]:
    if not heap:
        return None
    n = len(heap)
    nodes = [Node(heap[i]) for i in range(n)]
    if use_depth_colors:
        for i in range(n):
            nodes[i].color = _depth_color(i, n - 1)
    for i in range(n):
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < n:
            nodes[i].left = nodes[li]
        if ri < n:
            nodes[i].right = nodes[ri]
    return nodes[0]


def visualize_heap(heap: List[int], title: str = "Візуалізація бінарної купи") -> None:
    root = heap_to_tree(heap, use_depth_colors=True)
    if root is None:
        plt.figure(figsize=(6, 4))
        plt.title(title)
        plt.text(0.5, 0.5, "Купа порожня", ha="center", va="center")
        plt.axis("off")
        plt.show()
        return
    draw_tree(root, title=title)


if __name__ == "__main__":

    lh= [3, 8, 5, 10, 1, 2, 16, 12, 15, 18, 20, 25, 30, 4, 6]
    heapq.heapify(lh)
    print("Мін-купа у вигляді списку:", lh)
    visualize_heap(lh, title="Візуалізація мін-купи")

   
   
