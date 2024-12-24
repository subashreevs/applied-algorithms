from collections import defaultdict

def influencer_network(n: int, connections: list[list[int]]) -> list[list[int]]:
    # Build the graph in reverse: who influences whom
    graph = defaultdict(list)
    for a, b in connections:
        graph[b].append(a)
    
    # Cache to avoid recomputation
    reachable_cache = {}

    def dfs(node):
        if node in reachable_cache:
            return reachable_cache[node]
        reachable = set()
        for neighbor in graph[node]:
            reachable.add(neighbor)
            reachable.update(dfs(neighbor))
        reachable_cache[node] = reachable
        return reachable

    result = []
    for i in range(n):
        influencers = sorted(dfs(i))
        result.append(influencers)
    
    return result

# Test cases
n1 = 8
connections1 = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
print(influencer_network(n1, connections1))
# Expected Output: [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]

n2 = 5
connections2 = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(influencer_network(n2, connections2))
# Expected Output: [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]