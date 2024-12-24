from collections import defaultdict
import heapq
def bestPath(n, roads, src, dst, maxStops):
    graph = defaultdict(list)
    for u, v, cost in roads:
        graph[u].append((v, cost))
    
    pq = [(0, src, 0)]
    
    while pq:
        risk, node, stops = heapq.heappop(pq)
        
        if node == dst:
            return risk
        
        if stops > maxStops:
            continue
        
        for neighbor, cost in graph[node]:
            heapq.heappush(pq, (risk + cost, neighbor, stops + 1))
    
    return -1

# Test cases
def test_bestPath():
    test_cases = [
        {
            "n": 3,
            "roads": [[0, 1, 200], [0, 2, 600], [1, 2, 300]],
            "begin": 0,
            "end": 2,
            "K": 1,
            "expected": 500
        },
        {
            "n": 4,
            "roads": [[0, 1, 200], [1, 2, 300], [2, 3, 400]],
            "begin": 0,
            "end": 3,
            "K": 1,
            "expected": -1
        },
        {
            "n": 1,
            "roads": [],
            "begin": 0,
            "end": 0,
            "K": 0,
            "expected": 0
        },
        {
            "n": 4,
            "roads": [[0, 1, 100], [0, 2, 200], [1, 3, 100], [2, 3, 100]],
            "begin": 0,
            "end": 3,
            "K": 1,
            "expected": 200
        },
        {
            "n": 5,
            "roads": [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 4, 500], [4, 3, 50]],
            "begin": 0,
            "end": 3,
            "K": 3,
            "expected": 350
        },
    ]
    
    for i, test in enumerate(test_cases):
        result = bestPath(test["n"], test["roads"], test["begin"], test["end"], test["K"])
        print(f"Test case {i + 1}: {'Passed' if result == test['expected'] else 'Failed'}")
        if result != test['expected']:
            print(f" Expected: {test['expected']}, Got: {result}")

# Run the test function
test_bestPath()