from collections import defaultdict, deque

def processOperations(n: int, operations: List[Tuple[int, Union[str, Tuple[str, int]]]])-> List[str]:# Hard drive storage: maps movie name to (rating, access_count, timestamp)
    hard_drive = {}
    # Access count tracking for each movie
    access_count = defaultdict(int)
    # A deque to maintain the order of access for tie-breaking
    access_order = deque()
    # A time counter to track when movies are accessed
    time = 0
    result = []
    
    for operation in operations:
        if operation[0] == 1:
            # Check if movie/series is present on hard drive
            movie = operation[1]
            if movie in hard_drive:
                # Increase access count and update access order and timestamp
                access_count[movie] += 1
                access_order.append((movie, time))
                time += 1
                result.append(hard_drive[movie][0])  # Append the rating
            else:
                result.append(-1)  # Movie is not found
        elif operation[0] == 2:
            # Add or update the rating of movie/series
            movie, rating = operation[1]
            if movie in hard_drive:
                # Update the rating and increase access count
                hard_drive[movie] = (rating, access_count[movie] + 1, time)
                access_count[movie] += 1
                access_order.append((movie, time))
                time += 1
            else:
                # Hard drive is full, need to evict if necessary
                if len(hard_drive) == n:
                    # Find the least frequently used movie with the earliest access time
                    min_access = min(access_count.values())
                    candidates = []
                    for m in hard_drive:
                        if access_count[m] == min_access:
                            candidates.append(m)
                    # Sort candidates by access time (the first one is the oldest)
                    candidates.sort(key=lambda x: hard_drive[x][2])
                    to_remove = candidates[0]
                    # Remove the least accessed and oldest movie
                    del hard_drive[to_remove]
                    del access_count[to_remove]
                
                # Add the new movie/series
                hard_drive[movie] = (rating, 1, time)
                access_count[movie] = 1
                access_order.append((movie, time))
                time += 1
    
    return result




# n = 2
# operations = [
# (1, "GOT"), # Check if "GOT" is present
# (2, ("GOT", 9)), # Add "GOT" with rating 9
# (1, "GOT"), # Check if "GOT" is present
# (2, ("NARUT", 10)), # Add "NARUT" with rating 10
# (1, "NARUT"), # Check if "NARUT" is present
# (2, ("BARUT", 6)), # Add "BARUT" with rating 6
# (1, "GOT"), # Check if "GOT" is present
# (1, "BARUT"), # Check if "BARUT" is present
# ]

# print(processOperations(n, operations))
