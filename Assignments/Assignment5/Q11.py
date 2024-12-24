def countComponents(n: int, edges: list[list[int]]) -> int:
    # Initialize parent and rank
    parent = list(range(n))
    rank = [0] * n

    # Find operation with path compression
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    # Union operation with rank optimization
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    # Process all edges
    for a, b in edges:
        union(a, b)

    # Count unique roots
    return len(set(find(x) for x in range(n)))

# Test cases
n1 = 5
edges1 = [[0, 1], [1, 2], [3, 4]]
print(countComponents(n1, edges1))  # Expected Output: 2

n2 = 6
edges2 = [[0, 1], [1, 2], [2, 3], [4, 5]]
print(countComponents(n2, edges2))  # Expected Output: 2