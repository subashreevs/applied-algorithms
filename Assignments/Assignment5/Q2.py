import heapq
from collections import defaultdict

def constrainedNetwork(checkpoints: int, paths: int, network: list[tuple[int, int, int]]) -> int:
    # Build graph representation
    graph = defaultdict(list)
    for a, b, d in network:
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    # Min-heap to store (total_cost, current_node, max_difficulty_allowed)
    heap = [(0, 1, float('inf'))]  # (cost, node, max_difficulty)
    visited = {}
    
    while heap:
        cost, node, max_difficulty = heapq.heappop(heap)
        
        # If we reach the last checkpoint
        if node == checkpoints:
            return cost
        
        if (node, max_difficulty) in visited and visited[(node, max_difficulty)] <= cost:
            continue
        
        visited[(node, max_difficulty)] = cost
        
        for neighbor, difficulty in graph[node]:
            if difficulty <= max_difficulty:  # Ensure difficulty constraint
                heapq.heappush(heap, (cost + difficulty, neighbor, difficulty))
    
    return -1  # If no path found

# Test cases
checkpoints1, paths1, network1 = 5, 6, [(1, 2, 3), (2, 3, 2), (3, 5, 1), (1, 4, 4), (4, 5, 3), (2, 4, 1)]
print(constrainedNetwork(checkpoints1, paths1, network1))  # Output: 6

checkpoints2, paths2, network2 = 5, 3, [(1, 2, 1), (2, 3, 2), (4, 5, 3)]
print(constrainedNetwork(checkpoints2, paths2, network2))  # Output: -1
