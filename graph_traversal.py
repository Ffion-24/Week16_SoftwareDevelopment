from collections import deque

print("start")
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def bfs_traversal(g, start):
    visited = set([start])   # initialize with start
    order = []
    q = deque([start])

    while q:
        node = q.popleft()
        order.append(node)

        for nbr in g.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)

    return order

print(bfs_traversal(graph, "A"))