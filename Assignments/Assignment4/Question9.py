from typing import List, Tuple  # Import necessary types for type hinting

def min_rooms_required(arrival_departure_times: List[Tuple[int, int]]) -> int:
    # Separate and sort arrival and departure times into two individual lists
    sorted_arrival_times = sorted([arrival for arrival, departure in arrival_departure_times])
    sorted_departure_times = sorted([departure for arrival, departure in arrival_departure_times])

    # Initialize room counters: current rooms in use and maximum rooms needed
    current_rooms_in_use = 0
    maximum_rooms_needed = 0
    arrival_pointer, departure_pointer = 0, 0  # Pointers to traverse the arrival and departure lists
    total_guests = len(sorted_arrival_times)  # Total number of guests (length of the arrival list)

    # Use two pointers to traverse the sorted arrival and departure lists
    while arrival_pointer < total_guests:
        # If the next arrival occurs before or at the next departure, a new room is needed
        if sorted_arrival_times[arrival_pointer] <= sorted_departure_times[departure_pointer]:
            current_rooms_in_use += 1  # Increment rooms in use for the arriving guest
            # Update maximum rooms needed if the current count exceeds previous maximum
            maximum_rooms_needed = max(maximum_rooms_needed, current_rooms_in_use)
            arrival_pointer += 1  # Move to the next arrival
        else:
            # A guest departs, so a room is freed up
            current_rooms_in_use -= 1  # Decremenwwt rooms in use as one guest departs
            departure_pointer += 1  # Move to the next departure

    # Return the maximum number of rooms needed to accommodate all guests
    return maximum_rooms_needed

# # Example usage
# example_arrival_departure_times = [(1, 2), (2, 3), (4, 4)]
# print(min_rooms_required(example_arrival_departure_times))  # Expected output: 2
