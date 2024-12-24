from typing import List, Tuple
from collections import defaultdict

def MostFestiveExperience(n: int, highways: List[Tuple[int, int]], IsDiwali: List[int]) -> List[int]:
    # Adjacency list to represent the network of cities
    city_network = defaultdict(list)
    for city1, city2 in highways:
        city_network[city1].append(city2)
        city_network[city2].append(city1)
    
    # Array to store the difference between celebrating and non-celebrating cities
    celebration_diff = [0] * (n + 1)
    # Result array to store the maximum difference for each city
    result = [0] * n

    def calculate_difference(city, parent):
        # Initialize difference for the current city
        diff = 1 if IsDiwali[city - 1] == 1 else -1
        # Traverse neighbors of the current city
        for neighbor in city_network[city]:
            if neighbor != parent:
                child_diff = calculate_difference(neighbor, city)
                if child_diff > 0:
                    diff += child_diff
        celebration_diff[city] = diff
        return diff
    
    def distribute_difference(city, parent):
        # Store the calculated difference for the current city
        result[city - 1] = celebration_diff[city]
        # Traverse neighbors of the current city
        for neighbor in city_network[city]:
            if neighbor != parent:
                # Save contributions before modifying them
                parent_contribution = celebration_diff[city]
                child_contribution = celebration_diff[neighbor]
                
                # Adjust differences for moving root to neighbor
                if child_contribution > 0:
                    celebration_diff[city] -= child_contribution
                
                if celebration_diff[city] > 0:
                    celebration_diff[neighbor] += celebration_diff[city]
                
                # Recurse for the neighbor as the new root
                distribute_difference(neighbor, city)
                
                # Restore contributions after recursion
                celebration_diff[city] = parent_contribution
                celebration_diff[neighbor] = child_contribution
    
    # Perform initial DFS to calculate differences starting from city 1
    calculate_difference(1, -1)
    # Perform second DFS to distribute differences and calculate results
    distribute_difference(1, -1)
    
    return result