from collections import defaultdict

def princeJourney(v, routes, home, target):
    if home == target:
        return True
    
    graph = defaultdict(list)
    for a, b in routes:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    stack = [home]
    
    while stack:
        current = stack.pop()
        if current == target:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return False

v1, routes1, home1, target1 = 3, [[0, 1], [1, 2], [2, 0]], 0, 2
print(princeJourney(v1, routes1, home1, target1))

v2, routes2, home2, target2 = 6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 4
print(princeJourney(v2, routes2, home2, target2))
