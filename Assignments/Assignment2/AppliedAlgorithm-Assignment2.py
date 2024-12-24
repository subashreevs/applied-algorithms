from typing import List
from collections import deque
from collections import defaultdict
import re
from collections import deque
import random

# QUESTION 1

# Function to fetch the top element of the stack
def stackPeek(stack: List):
    # If the stack is empty, return -1
    if not stack:
        return -1
    else:
        # Return the last element of the stack (top element)
        return stack[-1]

def treasure_seq(target: List[int], n: int) -> List[str]:
    i = 1  # Counter for elements from 1 to n
    j = 0  # Counter for elements in the target list
    stack = []  # Initialize an empty stack
    output = []  # Initialize an empty output list to record operations
    
    # Loop until we have processed all elements from 1 to n or found all target elements
    while i <= n and j < len(target):
        # Push the current element onto the stack
        stack.append(i)
        output.append("Push")  # Record the operation
        
        # Check if the top of the stack matches the current target element
        if stackPeek(stack) == target[j]:
            j += 1  # Move to the next target element if there's a match
        else:
            # If there's no match, pop the top element from the stack
            stack.pop()
            output.append("Pop")  # Record the operation
        
        i += 1  # Increment the counter for the next element

    # Return the list of operations recorded in the output
    return output


# QUESTION 2

# Class to represent a node in a singly linked list
class Node:
    def __init__(self, val):
        self.val = val  # Initialize the node's value
        self.next = None  # Initialize the next pointer to None


# Class to represent a queue using a linked list
class Queue_LL:
    def __init__(self):
        self.head = None  # Initialize the head of the queue to None
        self.tail = None  # Initialize the tail of the queue to None
    
    # Method to add a value to the end of the queue
    def enqueue(self, val: int) -> None:
        new_node = Node(val)  # Create a new node with the given value
        if not self.tail:  # Check if the queue is empty (no tail)
            # If the queue is empty, set both head and tail to the new node
            self.head = self.tail = new_node
        else:
            # Link the new node to the end of the queue
            self.tail.next = new_node  # Set the current tail's next to the new node
            self.tail = new_node  # Update the tail to the new node
    
    # Method to remove and return a value from the front of the queue
    def dequeue(self) -> int:
        if not self.head:  # Check if the queue is empty (no head)
            return None  # If the queue is empty, return None
        dequeue_val = self.head.val  # Store the value at the head of the queue
        self.head = self.head.next  # Move the head pointer to the next node
        if not self.head:  # If the queue is now empty after dequeueing
            self.tail = None  # Set the tail to None as well
        
        return dequeue_val  # Return the dequeued value
    
    # Method to convert the queue into a list
    def QueueToList(self) -> list[int]:
        result_list = []  # Initialize an empty list to store the queue elements
        curr = self.head  # Start from the head of the queue
        while curr:  # Loop through the linked list until the end
            result_list.append(curr.val)  # Append the current node's value to the list
            curr = curr.next  # Move to the next node in the queue
        return result_list  # Return the list of queue elements


# QUESTION 3

def spiritualArithmetic(incantation: list[str]) -> int:
    # Initialize an empty stack to hold numbers
    stack = []
    
    if(len(incantation) == 1):
        return int(incantation[0])

    # Iterate through each token in the input list
    for i in incantation:
      
        # Check if the current token is an operator
        if i in "+-/*":
            # Pop the top two numbers from the stack for the operation
            int2 = int(stack.pop())  # Second operand
            int1 = int(stack.pop())  # First operand

            # Perform the appropriate operation based on the operator
            if i == '+':
                res = int1 + int2  # Addition
            elif i == "-":
                res = int1 - int2  # Subtraction
            elif i == "/":
                res = int(int1/int2)  # Division
            elif i == "*":
                res = int1 * int2  # Multiplication
            
            # Push the result of the operation back onto the stack
            stack.append(res)
        else:
            # If the token is a number, convert it to an integer and push it onto the stack
            stack.append(i)
        
        # Print the current state of the stack for debugging purposes
        print(stack)

    # The final result will be the only element left in the stack
    return stack[0]


# QUESTION 4

def largestArea(blocks: list[int]) -> int:
    # Append a 0 height at the end to ensure we process all heights in the stack
    blocks.append(0)
    max_area = 0
    stack = []  # Stack will store indices of the blocks

    for i in range(len(blocks)):
        # While the current block is smaller than the block at the top of the stack
        while stack and blocks[i] < blocks[stack[-1]]:
            h = blocks[stack.pop()]  # The height of the rectangle
            # Calculate the width based on the index where we popped
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)

    return max_area


# QUESTION 5

def arrangePerformers(nums):
    # Sort the numbers in descending order
    nums.sort(reverse=True)  
    # Initialize an empty deque to store the arrangement
    queue = deque()          
    
    # Iterate through each number in the sorted list
    for i in nums:           
        # If the queue is not empty
        if queue:            
            # Move the last element to the front
            queue.appendleft(queue.pop())  
        # Add the current number to the front of the queue
        queue.appendleft(i)  

    # Convert the deque back to a list and return it
    return list(queue)    


# QUESTION 6

# Function to count the number of atoms in a given chemical formula
def atom_counter(formula: str) -> str:
    inp_stack = [defaultdict(int)]  # Initialize a stack with a defaultdict to count elements
    i = 0  # Initialize an index to traverse the formula
    while i < len(formula):  # Loop through each character in the formula
        if formula[i].isalpha():  # Check if the character is an alphabet (element symbol)
            each_ele = formula[i]  # Store the current element symbol
            i += 1  # Move to the next character
            if i < len(formula) and formula[i].islower():  # Check for lowercase letters
                each_ele += formula[i]  # Append lowercase letter to the element symbol
                i += 1  # Move to the next character
            count = 0  # Initialize count for the current element
            while i < len(formula) and formula[i].isdigit():  # Check for digits following the element
                count = count * 10 + int(formula[i])  # Build the count number
                i += 1  # Move to the next character
            if count == 0:  # If no digits followed, set count to 1
                count = 1
            inp_stack[-1][each_ele] += count  # Update the count of the element in the top of the stack
        
        elif formula[i] == '(':  # Check for opening parenthesis
            inp_stack.append(defaultdict(int))  # Push a new defaultdict onto the stack for new group
            i += 1  # Move to the next character
        
        elif formula[i] == ')':  # Check for closing parenthesis
            i += 1  # Move to the next character
            count = 0  # Initialize count for the group
            while i < len(formula) and formula[i].isdigit():  # Check for digits following the closing parenthesis
                count = count * 10 + int(formula[i])  # Build the count number
                i += 1  # Move to the next character
            if count == 0:  # If no digits followed, set count to 1
                count = 1
            temp_count = inp_stack.pop()  # Pop the last element (group) from the stack
            for each_ele, c in temp_count.items():  # Iterate over the elements in the popped group
                inp_stack[-1][each_ele] += c * count  # Update the counts in the previous group
    
    final_count = inp_stack.pop()  # Pop the final count dictionary from the stack
    res = []  # Initialize a list to store the result
    for element in sorted(final_count.keys()):  # Sort the elements alphabetically
        count = final_count[element]  # Get the count for the element
        res.append(f"{element}{count if count > 1 else ''}")  # Append the element and its count (if > 1)
    
    return ''.join(res)  # Join the list into a string and return it


# QUESTION 7

# Function to determine the checkout counter times based on arrival times and actions
def checkout_counter_times(arrival, action):
    n = len(arrival)  # Get the number of customers
    res = [-1] * n  # Initialize result list to store times, defaulting to -1
    queue_checkout = deque()  # Queue for checkout actions
    queue_return = deque()  # Queue for return actions
    
    time = 0  # Initialize time counter
    previous_action = -1  # Track the last action performed (0 for checkout, 1 for return)
    
    i_counter = 0  # Index to track customer actions in the arrival list
    
    # Loop until all customers are processed and both queues are empty
    while i_counter < n or queue_checkout or queue_return:
        # Process arrivals at the current time
        while i_counter < n and arrival[i_counter] == time:
            if action[i_counter] == 0:  # If the action is checkout
                queue_checkout.append(i_counter)  # Add the customer to the checkout queue
            else:  # If the action is return
                queue_return.append(i_counter)  # Add the customer to the return queue
            i_counter += 1  # Move to the next customer in the arrival list
        
        # If there are customers waiting in either queue
        if queue_checkout or queue_return:
            # Determine which queue to process based on the last action
            if previous_action == 0:  # Last action was checkout
                if queue_checkout:  # If there are customers waiting to checkout
                    current = queue_checkout.popleft()  # Process the next checkout customer
                    res[current] = time  # Record the time of checkout
                    previous_action = 0  # Update the last action to checkout
                elif queue_return:  # If no checkout customers, process return
                    current = queue_return.popleft()  # Process the next return customer
                    res[current] = time  # Record the time of return
                    previous_action = 1  # Update the last action to return
            else:  # Last action was return or none
                if queue_return:  # If there are customers waiting to return
                    current = queue_return.popleft()  # Process the next return customer
                    res[current] = time  # Record the time of return
                    previous_action = 1  # Update the last action to return
                elif queue_checkout:  # If no return customers, process checkout
                    current = queue_checkout.popleft()  # Process the next checkout customer
                    res[current] = time  # Record the time of checkout
                    previous_action = 0  # Update the last action to checkout
        else:
            previous_action = -1  # Reset previous action if no customers are waiting
        
        time += 1  # Increment the time counter
    
    return res  # Return the list of times for each customer


# QUESTION 8

class quarryPieLine:
    def __init__(self):
        self.stack_memory = []  # Initialize an empty list to act as the underlying storage
        self.count = 0  # Initialize a counter to keep track of the total number of elements added
 
    def joinInFront(self):
        self.count += 1  # Increment the count for a new element
        self.stack_memory.insert(0, self.count)  # Insert the new element at the front of the list
 
    def joinInMiddle(self):
        self.count += 1  # Increment the count for a new element
        if not self.stack_memory:  # If the list is empty
            self.stack_memory.append(self.count)  # Add the new element to the list
        else:
            middle_ele = len(self.stack_memory) // 2  # Calculate the middle index
            self.stack_memory.insert(middle_ele, self.count)  # Insert the new element at the middle
 
    def joinInBack(self):
        self.count += 1  # Increment the count for a new element
        self.stack_memory.append(self.count)  # Add the new element to the end of the list
 
    def removeFromFront(self):
        if self.stack_memory:  # Check if the list is not empty
            self.stack_memory.pop(0)  # Remove the element from the front
 
    def removeFromMiddle(self):
        if self.stack_memory:  # Check if the list is not empty
            middle_ele = (len(self.stack_memory) - 1) // 2  # Calculate the middle index
            self.stack_memory.pop(middle_ele)  # Remove the element from the middle
 
    def removeFromBack(self):
        if self.stack_memory:  # Check if the list is not empty
            self.stack_memory.pop()  # Remove the element from the end of the list
 
    def whoIsFront(self) -> int:
        return self.stack_memory[0] if self.stack_memory else -1  # Return the front element or -1 if empty
 
    def whoIsMiddle(self) -> int:
        if not self.stack_memory:  # Check if the list is empty
            return -1  # Return -1 if empty
        middle_ele = (len(self.stack_memory) - 1) // 2  # Calculate the middle index
        return self.stack_memory[middle_ele]  # Return the middle element
 
    def whoIsBack(self) -> int:
        return self.stack_memory[-1] if self.stack_memory else -1  # Return the last element or -1 if empty


# QUESTION 9

class amor_dict:
    def __init__(self, num_list=[]):
        self.levels = {}  # Initialize a dictionary to store levels and their corresponding sorted lists
        for each_num in num_list:  # Insert each number from the initial list into the amor_dict
            self.insert(each_num)

    def insert(self, num):
        new_lev = 0  # Start from level 0 for insertion
        temp_mem = [num]  # Create a temporary list to hold the number being inserted
        
        # Loop to find the correct level for insertion
        while new_lev in self.levels:
            if len(self.levels[new_lev]) < 2 ** new_lev:  # Check if the current level can accept more numbers
                self.levels[new_lev] = self._merge(self.levels[new_lev], temp_mem)  # Merge and insert
                return
            else:  # If the current level is full
                # Merge the existing level with the temp memory and delete the full level
                temp_mem = self._merge(self.levels[new_lev], temp_mem)
                del self.levels[new_lev]  # Remove the full level
                new_lev += 1  # Move to the next level
        self.levels[new_lev] = temp_mem  # Insert the temp memory at the new level
        
    def search(self, num):
        # Iterate through the levels in sorted order to search for the number
        for level in sorted(self.levels.keys()):
            if self._binary_search(self.levels[level], num):  # Use binary search for efficiency
                return level  # Return the level where the number is found
        return -1  # Return -1 if the number is not found in any level

    def print(self):
        maximum_lev = max(self.levels.keys(), default=-1)  # Get the maximum level (or -1 if empty)
        # Create a list of lists representing each level's contents
        return [self.levels.get(i, []) for i in range(maximum_lev + 1)]
    
    def _merge(self, list1, list2):
        # Merges two sorted lists into one sorted list
        merged = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):  # Merge elements while both lists have elements
            if list1[i] <= list2[j]:  # Compare and add the smaller element
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        # Add any remaining elements from both lists
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged

    def _binary_search(self, arr, x):
        # Performs binary search to find an element in a sorted array
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2  # Calculate the mid index
            if arr[mid] == x:  # If the element is found
                return True
            elif arr[mid] < x:  # If the element is greater than the mid element
                low = mid + 1
            else:  # If the element is less than the mid element
                high = mid - 1
        return False  # Return False if the element is not found


# QUESTION 10

class Node:
    def __init__(self, val=None, next=None, down=None):
        self.val = val    # The value of the node
        self.next = next  # Pointer to the next node in the current level
        self.down = down  # Pointer to the node directly below in the lower level

class SkipList:
    def __init__(self):
        self.head = Node(-1)  # A sentinel node as the head of the skip list
        self.levels = 0       # Current number of levels in the skip list

    def search(self, target: int) -> bool:
        # Search for the target value in the skip list.
        current = self.head  # Start from the head (sentinel node)
        while current:  # Traverse the levels
            # Move right in the current level while the next node's value is less than the target
            while current.next and current.next.val < target:
                current = current.next
            # If the next node's value equals the target, return True
            if current.next and current.next.val == target:
                return True  # Target found
            current = current.down  # Move down one level to continue searching
        return False  # Target not found

    def insert(self, num: int) -> None:
        # Insert a number into the skip list.
        stack = []  # Stack to keep track of nodes for insertion at multiple levels
        current = self.head  # Start from the head (sentinel node)

        # Traverse the list to find the position to insert the new node
        while current:
            # Move right in the current level until the next node's value is greater than or equal to num
            while current.next and current.next.val < num:
                current = current.next
            stack.append(current)  # Save the current node to insert after it
            current = current.down  # Move down one level to continue searching for the next level

        # Determine how many levels the new node should occupy
        level = 0
        insert_level = random.random() < 0.5  # 50% chance to go up a level

        # Insert the new node at the appropriate levels based on the stack
        down_node = None  # Pointer to the node directly below in the next level
        while stack and (level == 0 or insert_level):
            current = stack.pop()  # Get the last saved node from the stack
            new_node = Node(num, next=current.next, down=down_node)  # Create the new node
            current.next = new_node  # Link the new node in the current level
            down_node = new_node  # Set the down pointer for the new level's node

            level += 1  # Increment the level count
            insert_level = random.random() < 0.5  # Randomly decide to go up another level

        # If we went higher than the current number of levels, add a new level
        if level > self.levels:
            # Create a new sentinel head for the new highest level
            self.head = Node(-1, down=self.head)
            self.levels += 1  # Increment the level count