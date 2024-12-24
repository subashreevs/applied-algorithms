def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    stack = [source]
    visited = set()

    while stack:
        node = stack.pop()
        if node == destination:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    
    return False


def validPathtest():
    return [
        [2, [[1, 0]], 0, 1],
        [3, [[0, 1], [1, 2], [2, 0]], 0, 2],
        [4, [[0, 2], [2, 3], [3, 1], [1, 0]], 1, 3],
        [5, [[1, 3], [3, 4], [4, 2], [2, 1]], 0, 4],
        [6, [[0, 4], [4, 5], [5, 3], [3, 0]], 2, 5],
    ]

for test_case in validPathtest():
    n = test_case[0]
    edges = test_case[1]
    source = test_case[2]
    destination = test_case[3]
    result = validPath(n, edges, source, destination)
    print(f"Test case: n={n}, edges={edges}, source={source}, destination={destination}")
    print(f"Result: {result}\n")
