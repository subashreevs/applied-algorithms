class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def findTreasure(head: ListNode) -> bool:
    if head is None:
        return True  # No loop, treasure found

    # Initialize two pointers, slow (tortoise) and fast (hare)
    slow = head
    fast = head

    while fast and fast.next:
        # Move slow pointer by one step
        slow = slow.next
        # Move fast pointer by two steps
        fast = fast.next.next

        # If slow and fast meet, there is a cycle
        if slow == fast:
            return False  # Treasure not found (cycle detected)

    return True  # Treasure found (no cycle)

# Test cases
# head = [ListNode(2), ListNode(1), ListNode(0), ListNode(10)]
# head[0].next = head[1]
# head[1].next = head[2]
# head[2].next = head[3]
# head[3].next = head[2]  # Creates a cycle at index 2
# print(findTreasure(head[0]))  # Output: False

# head = [ListNode(20), ListNode(-1)]
# head[0].next = head[1]
# head[1].next = head[0]  # Creates a cycle at index 0
# print(findTreasure(head[0]))  # Output: False

# head = [ListNode(12)]
# print(findTreasure(head[0]))  # Output: True
