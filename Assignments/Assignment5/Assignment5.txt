from collections import defaultdict
import heapq
from typing import List, Tuple
from collections import deque

# Code 1: This is the function where we check if we can go from home to target on some paths
def princeJourney(v, routes, home, target):
    # If the home and target are the same, then we are already there, so return True
    if home == target:
        return True
    
    # Make a map where we will store which places are connected to each other
    adjacency_list_graph = defaultdict(list)
    # Add all the routes to our map so we know who is connected to who
    for route_start, route_end in routes:
        adjacency_list_graph[route_start].append(route_end)
        adjacency_list_graph[route_end].append(route_start)
    
    # This will keep track of all the places we have visited so far
    visited_locations_set = set()
    # Start with our home and see where we can go from there
    locations_to_visit_stack = [home]
    
    # Keep going until we have checked all the places we can visit
    while locations_to_visit_stack:
        # Take one place from the list of places to check
        current_location = locations_to_visit_stack.pop()
        # If the current place is the target, we are done and return True
        if current_location == target:
            return True
        # If we have not been to this place before
        if current_location not in visited_locations_set:
            # Mark it as visited
            visited_locations_set.add(current_location)
            # Add all the places connected to this one to our list to check
            for neighbor_location in adjacency_list_graph[current_location]:
                if neighbor_location not in visited_locations_set:
                    locations_to_visit_stack.append(neighbor_location)
    
    # If we finished and never found the target, return False
    return False

# Test Case 1: Check if there is a path from home to target
# v1, routes1, home1, target1 = 3, [[0, 1], [1, 2], [2, 0]], 0, 2
# Explanation:
# - v1 represents the total number of nodes (3 nodes: 0, 1, and 2).
# - routes1 is a list of connections between nodes forming a cycle (0->1, 1->2, 2->0).
# - home1 is the starting point (node 0).
# - target1 is the destination point (node 2).
# Expected Output:
# Since all nodes are connected in a cycle, there exists a path from node 0 to node 2.
# print(princeJourney(v1, routes1, home1, target1))  # Output: True

# Test Case 2: Check if there is a path from home to target
# v2, routes2, home2, target2 = 6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 4
# Explanation:
# - v2 represents the total number of nodes (6 nodes: 0 to 5).
# - routes2 is a list of connections:
#   - Nodes 0, 1, and 2 are connected.
#   - Nodes 3, 4, and 5 are connected separately.
# - home2 is the starting point (node 0).
# - target2 is the destination point (node 4).
# Expected Output:
# Nodes 0 and 4 are in separate disconnected components, so there is no path between them.
# print(princeJourney(v2, routes2, home2, target2))  # Output: False



# Code 2: This is the function where we find the cheapest way to go from the first checkpoint to the last one
def constrainedNetwork(checkpoints, paths, network):
    # Make a map where we store which checkpoints are connected and the difficulty of going between them
    checkpoint_graph = defaultdict(list)
    # Add all the paths into the map so we know the difficulty for each route
    for path_start, path_end, difficulty_cost in network:
        checkpoint_graph[path_start].append((path_end, difficulty_cost))
        checkpoint_graph[path_end].append((path_start, difficulty_cost))
    
    # Use a heap to keep track of the cheapest path to check next
    cost_priority_queue = [(0, 1, float('inf'))]  # Start at checkpoint 1 with cost 0 and no difficulty limit
    visited_costs_dict = {}
    
    # Keep checking paths until there are no more paths to check
    while cost_priority_queue:
        # Take the path with the smallest cost
        current_cost, current_checkpoint, max_difficulty = heapq.heappop(cost_priority_queue)
        
        # If we reached the last checkpoint, return the cost
        if current_checkpoint == checkpoints:
            return current_cost
        
        # If we have already visited this place with a better or equal cost, skip it
        if (current_checkpoint, max_difficulty) in visited_costs_dict and visited_costs_dict[(current_checkpoint, max_difficulty)] <= current_cost:
            continue
        
        # Mark this place as visited with the current cost
        visited_costs_dict[(current_checkpoint, max_difficulty)] = current_cost
        
        # Go through all the places connected to this one
        for next_checkpoint, next_difficulty in checkpoint_graph[current_checkpoint]:
            # Only consider paths that are not harder than what we can handle
            if next_difficulty <= max_difficulty:
                heapq.heappush(cost_priority_queue, (current_cost + next_difficulty, next_checkpoint, next_difficulty))
    
    # If we finish and never reach the last checkpoint, return -1
    return -1

# # Test Case 1: Find the cheapest way to go from checkpoint 1 to 5
# checkpoints1, paths1, network1 = 5, 6, [(1, 2, 3), (2, 3, 2), (3, 5, 1), (1, 4, 4), (4, 5, 3), (2, 4, 1)]
# # Expected Output: The cheapest path has a total difficulty of 6.
# print(constrainedNetwork(checkpoints1, paths1, network1))  # Output: 6

# # Test Case 2: Check if a path exists from checkpoint 1 to 5
# checkpoints2, paths2, network2 = 5, 3, [(1, 2, 1), (2, 3, 2), (4, 5, 3)]
# # Expected Output: No path exists, so the output should be -1.
# print(constrainedNetwork(checkpoints2, paths2, network2))  # Output: -1




# Code 3: This is the function where we calculate how festive each city is based on celebrations and neighbors
def MostFestiveExperience(n, highways, IsDiwali):
    # Create a map that shows which cities are connected by highways
    city_graph = defaultdict(list)
    for city_a, city_b in highways:
        city_graph[city_a].append(city_b)
        city_graph[city_b].append(city_a)
    
    # This array will keep track of the difference between celebration and non-celebration cities
    celebration_differences = [0] * (n + 1)
    # This array will store the final result for each city
    festive_scores = [0] * n

    # This function calculates the difference for each city and its neighbors
    def calculate_difference(current_city, parent_city):
        # If the city celebrates Diwali, add 1; otherwise, subtract 1
        diff = 1 if IsDiwali[current_city - 1] == 1 else -1
        # Look at each neighbor of the current city
        for neighbor_city in city_graph[current_city]:
            # Skip the city we came from (the parent)
            if neighbor_city != parent_city:
                # Get the difference from the neighbor and add it to the current city if it's positive
                child_diff = calculate_difference(neighbor_city, current_city)
                if child_diff > 0:
                    diff += child_diff
        # Store the difference for the current city
        celebration_differences[current_city] = diff
        return diff
    
    # This function adjusts the difference for each city as we make it the new "root"
    def distribute_difference(city, parent_city):
        # Save the calculated difference for the current city
        festive_scores[city - 1] = celebration_differences[city]
        # Look at each neighbor of the current city
        for neighbor in city_graph[city]:
            # Skip the parent city
            if neighbor != parent_city:
                # Save the current contributions for later restoration
                parent_contribution = celebration_differences[city]
                child_contribution = celebration_differences[neighbor]
                
                # Remove the child's contribution from the parent and adjust the child's value
                if child_contribution > 0:
                    celebration_differences[city] -= child_contribution
                if celebration_differences[city] > 0:
                    celebration_differences[neighbor] += celebration_differences[city]
                
                # Call the function for the neighbor to calculate its result
                distribute_difference(neighbor, city)
                
                # Restore the original contributions after we are done
                celebration_differences[city] = parent_contribution
                celebration_differences[neighbor] = child_contribution
    
    # First, calculate the differences starting from city 1
    calculate_difference(1, -1)
    # Then adjust the differences for all cities
    distribute_difference(1, -1)
    
    # Return the final results for all cities
    return festive_scores

# Test cases

# Test Case 1
n1 = 4
highways1 = [(1, 2), (1, 3), (1, 4)]
IsDiwali1 = [0, 0, 1, 0]
print(MostFestiveExperience(n1, highways1, IsDiwali1))  # Expected Output: [0, -1, 1, -1]

# Test Case 2
n2 = 5
highways2 = [(1, 2), (2, 3), (3, 4), (3, 5)]
IsDiwali2 = [0, 1, 0, 1, 0]
print(MostFestiveExperience(n2, highways2, IsDiwali2))  # Expected Output: [0, 1, 1, 1, 0]




# Code 4: This function finds how many connected groups there are in the dominion
def findDominion(dominion):
    # Find the number of cities
    total_number_of_cities = len(dominion)
    # Keep track of which cities have been visited
    visited_cities = [False] * total_number_of_cities
    
    # This function visits all cities connected to the current one
    def depth_first_search(city_index):
        # Mark the current city as visited
        visited_cities[city_index] = True
        # Check all cities to see if they are connected
        for neighbor_city_index in range(total_number_of_cities):
            if dominion[city_index][neighbor_city_index] == 1 and not visited_cities[neighbor_city_index]:
                depth_first_search(neighbor_city_index)
    
    # Count how many separate groups there are
    total_dominion_groups = 0
    for current_city_index in range(total_number_of_cities):
        if not visited_cities[current_city_index]:  # If a city has not been visited yet
            depth_first_search(current_city_index)  # Visit all cities in this group
            total_dominion_groups += 1  # Add 1 to the group count
    
    # Return the total number of groups
    return total_dominion_groups

# # Test Case 1: Find the number of connected groups in the dominion
# dominion1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# # Explanation: The first two cities are connected, and the third city is isolated, making 2 groups.
# print(findDominion(dominion1))  # Expected Output: 2

# # Test Case 2: Find the number of connected groups where all cities are isolated
# dominion2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# # Explanation: Each city is isolated, so there are 3 separate groups.
# print(findDominion(dominion2))  # Expected Output: 3




# Code 5: This function checks if we can divide the cities into two teams so that every connection goes between the two teams
def Rangipur_Network(graph):
    # Find the number of cities
    total_number_of_cities = len(graph)
    # This array will keep track of which team each city belongs to (-1 means not decided yet)
    city_team_assignments = [-1] * total_number_of_cities
    
    # This function tries to color the cities using a queue
    def breadth_first_search(starting_city):
        # Start with the first city and color it with team 0
        cities_to_process_queue = deque([starting_city])
        city_team_assignments[starting_city] = 0
        
        # Keep going until all cities connected to this one are checked
        while cities_to_process_queue:
            # Take the next city to check
            current_city = cities_to_process_queue.popleft()
            # Look at all the neighbors of this city
            for neighbor_city in graph[current_city]:
                # If the neighbor is not colored, color it with the opposite team
                if city_team_assignments[neighbor_city] == -1:
                    city_team_assignments[neighbor_city] = 1 - city_team_assignments[current_city]
                    cities_to_process_queue.append(neighbor_city)
                # If the neighbor has the same color as the current city, it's not possible
                elif city_team_assignments[neighbor_city] == city_team_assignments[current_city]:
                    return False
        return True
    
    # Try to color all the cities starting from any uncolored city
    for city_index in range(total_number_of_cities):
        if city_team_assignments[city_index] == -1:
            if not breadth_first_search(city_index):
                return False  # If we find a conflict, return False
    
    return True  # If we color all cities without conflict, return True

# # Test Case 1: Check if cities in the graph can be divided into two teams
# graph1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
# # Explanation: There is at least one conflict where cities connected by an edge can't be divided into two teams.
# print(Rangipur_Network(graph1))  # Expected Output: False

# # Test Case 2: Check if cities in the graph can be divided into two teams without conflicts
# graph2 = [[1, 3], [0, 2], [1, 3], [0, 2]]
# # Explanation: The graph is bipartite, and cities can be divided into two teams with no conflicts.
# print(Rangipur_Network(graph2))  # Expected Output: True




# Code 6: This function finds the minimum cost to connect all points in a grid
def minCostConnectPoints(points):
    # Find the number of points
    total_number_of_points = len(points)
    # Keep track of which points have already been connected
    visited_points = [False] * total_number_of_points
    # Start with a heap to find the smallest distance to connect a point
    connection_priority_queue = [(0, 0)]  # Start with cost 0 at point 0
    # Keep track of the total cost and the number of edges we use
    total_connection_cost = 0
    number_of_connected_edges = 0

    # Keep going until we have used enough edges to connect all points
    while number_of_connected_edges < total_number_of_points:
        # Take the smallest cost edge from the heap
        current_cost, current_point = heapq.heappop(connection_priority_queue)
        # If the point is already connected, skip it
        if visited_points[current_point]:
            continue
        # Mark the point as connected
        visited_points[current_point] = True
        # Add the cost to the total
        total_connection_cost += current_cost
        # Count this edge as used
        number_of_connected_edges += 1

        # Check all other points to see the distance to the current point
        for next_point in range(total_number_of_points):
            if not visited_points[next_point]:
                # Calculate the Manhattan distance between points
                distance_between_points = abs(points[current_point][0] - points[next_point][0]) + abs(points[current_point][1] - points[next_point][1])
                # Add this distance to the heap
                heapq.heappush(connection_priority_queue, (distance_between_points, next_point))

    # Return the total cost to connect all points
    return total_connection_cost

# # Test Case 1: Connect points with minimum cost in a small grid
# points1 = [[3, 12], [-2, 5], [-4, 1]]
# # Explanation: The Manhattan distances between points are calculated, and the minimum cost to connect all points is found.
# print(minCostConnectPoints(points1))  # Expected Output: 18

# # Test Case 2: Connect points in a larger grid
# points2 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
# # Explanation: The minimum cost to connect all points using the Manhattan distances is calculated.
# print(minCostConnectPoints(points2))  # Expected Output: 20




# Code 7: This function finds the cheapest way to travel between two cities with at most K stops
def findCheapestLandTransport(total_number_of_cities, travel_routes, source_city, destination_city, maximum_allowed_stops):
    # Make a map to store which cities are connected and the cost to travel between them
    city_connection_graph = defaultdict(list)
    for route_start, route_end, travel_cost, travel_mode in travel_routes:
        city_connection_graph[route_start].append((route_end, travel_cost))
    
    # Use a heap to keep track of the cheapest way to get to each city
    travel_priority_queue = [(0, source_city, maximum_allowed_stops + 1)]  # Start at the source city with 0 cost and K+1 stops allowed
    
    # Keep checking routes until we find the destination or run out of options
    while travel_priority_queue:
        # Take the cheapest route from the heap
        current_cost, current_city, remaining_stops = heapq.heappop(travel_priority_queue)
        
        # If we reach the destination, return the cost
        if current_city == destination_city:
            return current_cost
        
        # If we still have stops left, check all the neighbors of the current city
        if remaining_stops > 0:
            for neighboring_city, travel_cost in city_connection_graph[current_city]:
                heapq.heappush(travel_priority_queue, (current_cost + travel_cost, neighboring_city, remaining_stops - 1))
    
    # If we finish and can't find a way to the destination, return -1
    return -1

# # Test Case 1: Find the cheapest transport with up to 1 stop
# n1 = 4
# routes1 = [[0, 1, 100, 'bus'], [1, 2, 100, 'train'], [2, 3, 100, 'train'], [0, 3, 500, 'bus']]
# src1, dst1, K1 = 0, 3, 1
# # Explanation: The cheapest route to get from city 0 to city 3 with at most 1 stop is calculated.
# print(findCheapestLandTransport(n1, routes1, src1, dst1, K1))  # Expected Output: 500

# # Test Case 2: Calculate the minimum cost between cities with another stop allowance
# n2 = 3
# routes2 = [[0, 1, 300, 'bus'], [1, 2, 300, 'bus'], [0, 2, 700, 'train']]
# src2, dst2, K2 = 0, 2, 1
# # Explanation: The path with the minimum cost and allowed stops is selected.
# print(findCheapestLandTransport(n2, routes2, src2, dst2, K2))  # Expected Output: 600

# # Test Case 3: No valid route exists within the allowed stops
# n3 = 3
# routes3 = [[0, 1, 100, 'train'], [1, 0, 100, 'bus']]
# src3, dst3, K3 = 0, 2, 1
# # Explanation: There is no path to get from city 0 to city 2 with at most 1 stop.
# print(findCheapestLandTransport(n3, routes3, src3, dst3, K3))  # Expected Output: -1




# Code 8: This function finds out who influences who in a big network of people
def influencer_network(total_number_of_people, influence_connections):
    # Make a map to store who is influenced by whom
    influence_graph = defaultdict(list)
    # Add all the connections so we know who can influence who directly
    for influencer_person, influenced_person in influence_connections:
        influence_graph[influenced_person].append(influencer_person)
    
    # Keep a cache so we don't repeat calculations for the same person
    influence_cache = {}

    # This function finds all the people who can influence a given person
    def calculate_influence_chain(person):
        # If we already know the result, return it
        if person in influence_cache:
            return influence_cache[person]
        # Start with an empty set of influencers
        total_influencers = set()
        # Check everyone who directly influences this person
        for direct_influencer in influence_graph[person]:
            # Add the direct influencer and everyone who influences them
            total_influencers.add(direct_influencer)
            total_influencers.update(calculate_influence_chain(direct_influencer))
        # Save the result in the cache and return it
        influence_cache[person] = total_influencers
        return total_influencers

    # For each person, find out who influences them and sort the results
    influence_results = []
    for person_index in range(total_number_of_people):
        sorted_influencers = sorted(calculate_influence_chain(person_index))
        influence_results.append(sorted_influencers)
    
    # Return the list of influencers for each person
    return influence_results

# # Test Case 1: Finding influencers in a large network
# n1 = 8
# connections1 = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
# # Explanation: Determines who influences whom based on the connections in the graph.
# print(influencer_network(n1, connections1))
# # Expected Output: [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]

# # Test Case 2: Checking complete influencer relationships in a dense network
# n2 = 5
# connections2 = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
# # Explanation: With a fully connected network, the influence graph expands to include all reachable nodes.
# print(influencer_network(n2, connections2))
# # Expected Output: [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]




# Code 9: This function counts the number of connected parts in a network of parentheses
def GraphInGokuldham(total_parentheses_count: int, parentheses_string: str) -> int:
    # This is a list where we will keep the positions of all the open parentheses
    list_of_open_parentheses_indices = []
    # This will keep track of how many groups or components we have found
    total_connected_components_count = 0

    # We are going to look at each character in the string of parentheses one by one
    for current_character_index, current_character_value in enumerate(parentheses_string):
        # If we see an open parenthesis, we add its position to our list
        if current_character_value == '(':
            list_of_open_parentheses_indices.append(current_character_index)
        else:
            # Otherwise, if it is a closing parenthesis
            if not list_of_open_parentheses_indices:
                # If we don't have any open parentheses left, it means this is a new component
                total_connected_components_count += 1
            else:
                # If we have an open parenthesis, we remove the last one we added
                previous_open_parenthesis_index = list_of_open_parentheses_indices.pop()
                # If this closing parenthesis is not right after the open one, it is a new component
                if previous_open_parenthesis_index != current_character_index - 1:
                    total_connected_components_count += 1

    # If there are any open parentheses left, each one is its own separate component
    total_connected_components_count += len(list_of_open_parentheses_indices)

    # We add one more because every graph starts with one component
    return total_connected_components_count + 1

# # Test cases for counting connected components in a parentheses graph

# # Test Case 1: Single complete pair of parentheses
# # Explanation: The graph has one component because the single pair of parentheses is connected.
# print(GraphInGokuldham(1, "()"))          # Expected Output: 1

# # Test Case 2: Mixed and nested parentheses
# # Explanation: The string contains two components: 
# # - The first pair "()" is a separate component.
# # - The remaining parentheses "()())" form a second component due to their nesting structure.
# print(GraphInGokuldham(3, "()(()))"))     # Expected Output: 2




# Code 10: This function finds the shortest cycle in a neighborhood where people want to walk without repeating streets
def festiveWalkPath(total_number_of_houses, street_connections):
    # Make a map of the neighborhood where each house is connected to others by streets
    neighborhood_street_graph = defaultdict(list)
    for house_start, house_end in street_connections:
        neighborhood_street_graph[house_start].append(house_end)
        neighborhood_street_graph[house_end].append(house_start)
    
    # This function uses BFS to find the shortest cycle starting from a house
    def breadth_first_search_for_cycle(starting_house):
        # Keep track of which houses we have visited and their distances
        visited_houses = [-1] * total_number_of_houses
        # Start the search with the first house
        houses_queue = deque([(starting_house, -1)])  
        visited_houses[starting_house] = 0
        
        # Keep checking houses until we find a cycle or finish
        while houses_queue:
            current_house, previous_house = houses_queue.popleft()
            # Look at all the connected houses
            for neighbor_house in neighborhood_street_graph[current_house]:
                # If we haven't visited this house, visit it now
                if visited_houses[neighbor_house] == -1:
                    visited_houses[neighbor_house] = visited_houses[current_house] + 1
                    houses_queue.append((neighbor_house, current_house))
                # If we find a house that is not the previous one, we found a cycle
                elif neighbor_house != previous_house:
                    return visited_houses[current_house] + visited_houses[neighbor_house] + 1
        return float('inf')

    # Try to find the shortest cycle starting from each house
    shortest_cycle_length = float('inf')
    for house_index in range(total_number_of_houses):
        shortest_cycle_length = min(shortest_cycle_length, breadth_first_search_for_cycle(house_index))
    
    # If we found a cycle, return its length; otherwise, return -1
    return -1 if shortest_cycle_length == float('inf') else shortest_cycle_length

# # Test cases for finding the shortest cycle in a neighborhood of houses connected by streets

# # Test Case 1: A neighborhood with multiple houses and streets forming a cycle
# # Explanation: The shortest cycle is formed by the houses [0, 1, 2, 3], making the cycle length 4.
# n1 = 6
# streets1 = [[0, 1], [1, 2], [2, 3], [3, 0], [3, 4], [4, 5]]
# print(festiveWalkPath(n1, streets1))  # Expected Output: 4

# # Test Case 2: A neighborhood with disconnected houses and no cycle
# # Explanation: The streets do not form a cycle, so the function returns -1.
# n2 = 6
# streets2 = [[1, 2], [2, 3], [4, 5]]
# print(festiveWalkPath(n2, streets2))  # Expected Output: -1




# Code 11: This function counts the number of connected parts in a network
def countComponents(total_nodes, edges):
    # Keep track of which group each node belongs to
    node_parent_references = list(range(total_nodes))
    # Keep track of the size of each group
    group_ranks = [0] * total_nodes

    # This function finds the leader of the group for a node
    def find_parent(node):
        if node_parent_references[node] != node:
            node_parent_references[node] = find_parent(node_parent_references[node])
        return node_parent_references[node]

    # This function joins two groups together
    def union_groups(node_a, node_b):
        root_a = find_parent(node_a)
        root_b = find_parent(node_b)
        if root_a != root_b:
            if group_ranks[root_a] > group_ranks[root_b]:
                node_parent_references[root_b] = root_a
            elif group_ranks[root_a] < group_ranks[root_b]:
                node_parent_references[root_a] = root_b
            else:
                node_parent_references[root_b] = root_a
                group_ranks[root_a] += 1

    # Join groups based on the edges
    for edge_start, edge_end in edges:
        union_groups(edge_start, edge_end)

    # Count how many unique leaders there are
    unique_groups = len(set(find_parent(node) for node in range(total_nodes)))
    return unique_groups

# # Test cases for counting the number of connected components in a network of nodes

# # Test Case 1: A network with 5 nodes and edges connecting some of them
# # Explanation: The network has two separate groups of connected nodes: [0, 1, 2] and [3, 4].
# n1 = 5
# edges1 = [[0, 1], [1, 2], [3, 4]]
# print(countComponents(n1, edges1))  # Expected Output: 2

# # Test Case 2: A network with 6 nodes and edges connecting some of them
# # Explanation: The network has two separate groups of connected nodes: [0, 1, 2, 3] and [4, 5].
# n2 = 6
# edges2 = [[0, 1], [1, 2], [2, 3], [4, 5]]
# print(countComponents(n2, edges2))  # Expected Output: 2