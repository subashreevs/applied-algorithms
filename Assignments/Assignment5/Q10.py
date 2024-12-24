from collections import defaultdict, deque
from typing import List

def festiveWalkPath(n: int, streets: List[List[int]]) -> int:
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v in streets:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs_find_cycle(start):
        visited = [-1] * n
        queue = deque([(start, -1)])  # (current_node, parent)
        visited[start] = 0
        
        while queue:
            current, parent = queue.popleft()
            for neighbor in graph[current]:
                if visited[neighbor] == -1:  # Not visited
                    visited[neighbor] = visited[current] + 1
                    queue.append((neighbor, current))
                elif neighbor != parent:  # Cycle detected
                    return visited[current] + visited[neighbor] + 1
        return float('inf')
    
    shortest_cycle = float('inf')
    for i in range(n):
        shortest_cycle = min(shortest_cycle, bfs_find_cycle(i))
    
    return -1 if shortest_cycle == float('inf') else shortest_cycle

# Test cases
n1 = 6
streets1 = [[0, 1], [1, 2], [2, 3], [3, 0], [3, 4], [4, 5]]
print(festiveWalkPath(n1, streets1))  # Expected Output: 4

n2 = 6
streets2 = [[1, 2], [2, 3], [4, 5]]
print(festiveWalkPath(n2, streets2))  # Expected Output: -1