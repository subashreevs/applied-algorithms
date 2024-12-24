import heapq  # Import heapq for priority queue functionality
from collections import Counter, deque  # Import Counter for task counting and deque for managing cooldowns

def lelouch_task_schedule(tasks: list[str], cooldown_interval: int) -> int:
    # Count the frequency of each task to know how often each needs to be scheduled
    task_frequency_counter = Counter(tasks)
    
    # Create a max heap using negative counts (since heapq is a min heap by default)
    max_heap_task_counts = [-task_count for task_count in task_frequency_counter.values()]
    heapq.heapify(max_heap_task_counts)  # Transform the list into a heap structure

    # Queue to track tasks currently in cooldown with their count and time when they can be executed again
    cooldown_queue_tracker = deque()
    current_time_unit = 0  # Initialize time tracker to zero

    # Process tasks until there are no more tasks in either the heap or the cooldown queue
    while max_heap_task_counts or cooldown_queue_tracker:
        current_time_unit += 1  # Increment the time with each iteration

        # Execute the most frequent task if the max heap has tasks
        if max_heap_task_counts:
            # Remove the highest frequency task (with a negative count to simulate max heap)
            current_task_count_remaining = heapq.heappop(max_heap_task_counts) + 1  # Increase count since it's negative
            if current_task_count_remaining != 0:
                # If there are still occurrences left for this task, add it to the cooldown queue
                cooldown_queue_tracker.append((current_task_count_remaining, current_time_unit + cooldown_interval))

        # Check if any task's cooldown period has ended and is ready to be re-added to the heap
        if cooldown_queue_tracker and cooldown_queue_tracker[0][1] == current_time_unit:
            # Pop the task from cooldown and push it back into the heap
            heapq.heappush(max_heap_task_counts, cooldown_queue_tracker.popleft()[0])

    # Return the total time units needed to complete all tasks with the given cooldowns
    return current_time_unit

# # Example usage
# tasks_example_1 = ["A", "A", "A", "B", "B", "B"]
# cooldown_interval_1 = 2
# print(lelouch_task_schedule(tasks_example_1, cooldown_interval_1))  # Expected output: 8

# tasks_example_2 = ["A", "C", "A", "B", "D", "B"]
# cooldown_interval_2 = 1
# print(lelouch_task_schedule(tasks_example_2, cooldown_interval_2))  # Expected output: 6

# tasks_example_3 = ["A", "A", "A", "B", "B", "B"]
# cooldown_interval_3 = 3
# print(lelouch_task_schedule(tasks_example_3, cooldown_interval_3))  # Expected output: 10