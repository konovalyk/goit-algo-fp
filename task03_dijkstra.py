
import heapq
from typing import Any, Dict, List, Optional, Tuple
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(G: nx.Graph, start: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]: 
    distances: Dict[Any, float] = {n: float('inf') for n in G.nodes}
    if start not in distances:
        raise ValueError(f"Start node '{start}' not in graph")
    distances[start] = 0.0
    previous: Dict[Any, Optional[Any]] = {n: None for n in G.nodes}

    heap: List[Tuple[float, Any]] = [(0.0, start)]
    visited: set[Any] = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if d > distances[u]:
            continue

        for v, attrs in G[u].items():
            w = float(attrs.get('weight', 1.0))
            nd = d + w
            if nd < distances[v]:
                distances[v] = nd
                previous[v] = u
                heapq.heappush(heap, (nd, v))

    return distances, previous


def reconstruct_path(previous: Dict[Any, Optional[Any]], start: Any, end: Any) -> List[Any]:
    path: List[Any] = []
    cur: Optional[Any] = end
    while cur is not None:
        path.append(cur)
        cur = previous[cur]
    path.reverse()
    return path if path and path[0] == start else []


def print_shortest_paths(G: nx.Graph, start: Any) -> None:
    distances, previous = dijkstra(G, start)

    print(f"\nНайкоротші шляхи від вершини '{start}':")
    print("-" * 60)
    print(f"{'До вершини':<15} {'Відстань':<15} {'Шлях':<30}")
    print("-" * 60)
    for node in sorted(G.nodes, key=str):
        d = distances.get(node, float('inf'))
        if d == float('inf'):
            path_str = 'недоступна'; dist_str = '∞'
        else:
            path = reconstruct_path(previous, start, node)
            path_str = ' → '.join(map(str, path)); dist_str = str(d)
        print(f"{str(node):<15} {dist_str:<15} {path_str:<30}")
    print("-" * 60)


def demo(G: nx.Graph, start: Any, title: str = "Демонстрація графа", layout: str = "spring") -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    print_shortest_paths(G, start)

    pos = nx.spring_layout(G) if layout == "spring" else nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=2)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    plt.title(title)
    plt.axis("off")
    plt.show()



if __name__ == "__main__":

    G1 = nx.Graph()
    G1.add_weighted_edges_from([
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
    ])

    G2 = nx.Graph()
    G2.add_weighted_edges_from([
        ("0", "1", 7),
        ("0", "2", 9),
        ("0", "5", 14),
        ("1", "2", 10),
        ("1", "3", 15),
        ("2", "3", 11),
        ("2", "5", 2),
        ("3", "4", 6),
        ("4", "5", 9),
    ])
    demo(G1, start="A", title="ПРИКЛАД 1")
    demo(G2, start="0", title="ПРИКЛАД 2")
