from collections import deque
from typing import Callable, Iterable, List, Optional

from heap_visualization import Node, draw_tree
from matplotlib import cm, colors as mpl_colors


TraversalFn = Callable[[Optional[Node]], List[Node]]


def _generate_gradient_colors(count: int, start: float = 0.25, end: float = 0.9, cmap=cm.Blues) -> List[str]:
    if count <= 0:
        return []
    step = end - start
    denom = max(1, count - 1)
    return [mpl_colors.to_hex(cmap(start + step * (i / denom))) for i in range(count)]


def _clone_tree(root: Optional[Node]) -> Optional[Node]:
    if root is None:
        return None
    root_clone = Node(root.val)
    queue = deque([(root, root_clone)])
    while queue:
        original, clone = queue.popleft()
        if original.left:
            clone_left = Node(original.left.val)
            clone.left = clone_left
            queue.append((original.left, clone_left))
        if original.right:
            clone_right = Node(original.right.val)
            clone.right = clone_right
            queue.append((original.right, clone_right))
    return root_clone


def bfs_traversal(root: Optional[Node]) -> List[Node]:
    order: List[Node] = []
    if root is None:
        return order
    queue: deque[Node] = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs_traversal(root: Optional[Node]) -> List[Node]:
    order: List[Node] = []
    if root is None:
        return order
    stack: List[Node] = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def _apply_colors(order: Iterable[Node], cmap=cm.Blues) -> List[str]:
    order_list = list(order)
    colors = _generate_gradient_colors(len(order_list), cmap=cmap)
    for node, color in zip(order_list, colors):
        node.color = color
    return colors


def visualize_traversal(root: Optional[Node], traversal: TraversalFn, title: str, cmap=cm.Blues) -> List[int]:
    cloned = _clone_tree(root)
    if cloned is None:
        return []
    order = traversal(cloned)
    _apply_colors(order, cmap=cmap)
    draw_tree(cloned, title=title)
    return [node.val for node in order]


def build_sample_tree() -> Node:
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root


if __name__ == "__main__":

    tree = build_sample_tree()

    bfs_order_vals = visualize_traversal(tree, bfs_traversal, title="BFS (ширина)", cmap=cm.Greens)
    print("BFS порядок відвідування:", bfs_order_vals)

    dfs_order_vals = visualize_traversal(tree, dfs_traversal, title="DFS (глибина)", cmap=cm.Blues)
    print("DFS порядок відвідування:", dfs_order_vals)