from typing import List

def findDominion(dominion: List[List[int]]) -> int:
    n = len(dominion)
    visited = [False] * n
    
    def dfs(node: int):
        visited[node] = True
        for neighbor in range(n):
            if dominion[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    
    dominion_count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            dominion_count += 1
    
    return dominion_count

# Test cases
dominion1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(findDominion(dominion1))  # Expected Output: 2

dominion2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(findDominion(dominion2))  # Expected Output: 3
