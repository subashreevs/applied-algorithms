from typing import List
from collections import deque

def Rangipur_Network(graph: List[List[int]]) -> bool:
    n = len(graph)
    color = [-1] * n  # -1 indicates uncolored, 0 for one team, 1 for the other
    
    def bfs(start: int) -> bool:
        queue = deque([start])
        color[start] = 0  # Start with color 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # If uncolored, assign opposite color
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # Conflict found
                    return False
        return True
    
    for i in range(n):
        if color[i] == -1:  # If the node hasn't been visited yet
            if not bfs(i):
                return False
    
    return True

# Test cases
graph1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(Rangipur_Network(graph1))  # Expected Output: False

graph2 = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(Rangipur_Network(graph2))  # Expected Output: True
