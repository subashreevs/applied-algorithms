import random

class Node:
    def __init__(self, val=None, next=None, down=None):
        self.val = val    # The value of the node
        self.next = next  # Pointer to the next node in the current level
        self.down = down  # Pointer to the node directly below in the lower level

class SkipList:
    def __init__(self):
        self.head = Node(-1)  # A sentinel node as the head of the skip list
        self.levels = 0       # Current number of levels

    def search(self, target: int) -> bool:
        """Search for the target value in the skip list."""
        current = self.head
        while current:
            while current.next and current.next.val < target:
                current = current.next
            if current.next and current.next.val == target:
                return True  # Target found
            current = current.down  # Move down one level
        return False  # Target not found

    def insert(self, num: int) -> None:
        """Insert a number into the skip list."""
        # Maintain a stack of nodes where the new node should be inserted
        stack = []
        current = self.head

        # Traverse the list and prepare to insert at multiple levels
        while current:
            while current.next and current.next.val < num:
                current = current.next
            stack.append(current)  # Save the current node to insert after it
            current = current.down  # Move down one level

        # Determine how many levels the new node should occupy
        level = 0
        insert_level = random.random() < 0.5  # 50% chance to go up a level

        # Insert the new node at the appropriate levels
        down_node = None
        while stack and (level == 0 or insert_level):
            current = stack.pop()
            new_node = Node(num, next=current.next, down=down_node)
            current.next = new_node
            down_node = new_node  # Set the down pointer for the next level up

            level += 1
            insert_level = random.random() < 0.5  # Randomly decide to go up another level

        # If we went higher than the current number of levels, add a new level
        if level > self.levels:
            self.head = Node(-1, down=self.head)  # New sentinel head for the new level
            self.levels += 1

# Example usage:
# sl = SkipList()
# sl.insert(1)  # None
# sl.insert(2)  # None
# sl.insert(3)  # None
# print(sl.search(4))  # False
# sl.insert(4)  # None
# print(sl.search(4))  # True
# print(sl.search(1))  # True
