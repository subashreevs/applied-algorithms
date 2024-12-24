from typing import List
import heapq

def minCostConnectPoints(points: List[List[int]]) -> int:
    n = len(points)
    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, point_index)
    total_cost = 0
    edges_used = 0

    while edges_used < n:
        cost, current = heapq.heappop(min_heap)
        if visited[current]:
            continue
        visited[current] = True
        total_cost += cost
        edges_used += 1

        for next_point in range(n):
            if not visited[next_point]:
                distance = abs(points[current][0] - points[next_point][0]) + abs(points[current][1] - points[next_point][1])
                heapq.heappush(min_heap, (distance, next_point))

    return total_cost

# Test cases
points1 = [[3, 12], [-2, 5], [-4, 1]]
print(minCostConnectPoints(points1))  # Expected Output: 18

points2 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(minCostConnectPoints(points2))  # Expected Output: 20
