from collections import deque

def checkout_counter_times(arrival, action):
    n = len(arrival)
    result = [-1] * n
    
    checkout_queue = deque()  # Queue for checkout actions (action[i] = 0)
    return_queue = deque()    # Queue for return actions (action[i] = 1)
    
    last_action = -1  # Initially no action performed (-1)
    current_time = 0   # To track the current time
    i = 0              # To track customers
    
    while i < n or checkout_queue or return_queue:
        # Add all customers arriving at the current time to the appropriate queue
        while i < n and arrival[i] == current_time:
            if action[i] == 0:
                checkout_queue.append(i)
            else:
                return_queue.append(i)
            i += 1
        
        # Choose which customer to serve based on the rules
        if last_action == 0:  # Last action was checkout
            if checkout_queue:
                customer = checkout_queue.popleft()
                result[customer] = current_time
                last_action = 0
            elif return_queue:
                customer = return_queue.popleft()
                result[customer] = current_time
                last_action = 1
        
        elif last_action == 1:  # Last action was return
            if return_queue:
                customer = return_queue.popleft()
                result[customer] = current_time
                last_action = 1
            elif checkout_queue:
                customer = checkout_queue.popleft()
                result[customer] = current_time
                last_action = 0
        
        else:  # No last action (initial case)
            if return_queue:
                customer = return_queue.popleft()
                result[customer] = current_time
                last_action = 1
            elif checkout_queue:
                customer = checkout_queue.popleft()
                result[customer] = current_time
                last_action = 0
        
        current_time += 1  # Move to the next second
    
    return result


arrival = [0,1,1,2,4]
action = [0,1,0,0,1]
print(checkout_counter_times(arrival, action))


arrival = [0,0,0]
action = [1,0,1]
print(checkout_counter_times(arrival, action))