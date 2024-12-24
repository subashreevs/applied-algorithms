from typing import List
import heapq
from collections import defaultdict

def findCheapestLandTransport(n: int, routes: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = defaultdict(list)
    
    # Build the graph
    for route in routes:
        u, v, cost, mode = route
        graph[u].append((v, cost))
    
    # Priority queue: (cost, current_city, stops_remaining)
    heap = [(0, src, K + 1)]
    
    while heap:
        cost, current_city, stops = heapq.heappop(heap)
        
        if current_city == dst:
            return cost
        
        if stops > 0:
            for neighbor, price in graph[current_city]:
                heapq.heappush(heap, (cost + price, neighbor, stops - 1))
    
    return -1

# Test cases
n1 = 4
routes1 = [[0, 1, 100, 'bus'], [1, 2, 100, 'train'], [2, 3, 100, 'train'], [0, 3, 500, 'bus']]
src1, dst1, K1 = 0, 3, 1
print(findCheapestLandTransport(n1, routes1, src1, dst1, K1))  # Expected Output: 500

n2 = 3
routes2 = [[0, 1, 300, 'bus'], [1, 2, 300, 'bus'], [0, 2, 700, 'train']]
src2, dst2, K2 = 0, 2, 1
print(findCheapestLandTransport(n2, routes2, src2, dst2, K2))  # Expected Output: 600

n3 = 3
routes3 = [[0, 1, 100, 'train'], [1, 0, 100, 'bus']]
src3, dst3, K3 = 0, 2, 1
print(findCheapestLandTransport(n3, routes3, src3, dst3, K3))  # Expected Output: -1
