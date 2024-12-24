class ListNode:
    def __init__(self, value=0, next_node=None):
        # Initialize the ListNode with a value and a pointer to the next node
        self.val = value
        self.next = next_node

def removeElements(head_node: ListNode, target_value: int) -> ListNode:
    # Base case: if the head_node is None, return None
    if not head_node:
        return None
    
    # Recursive call for the next node
    head_node.next = removeElements(head_node.next, target_value)
    
    # Check the current node's value
    if head_node.val == target_value:
        # Skip this node
        return head_node.next
    else:
        # Keep this node
        return head_node

# Helper function to create a linked list from a list of values
def create_linked_list(value_list):
    # If the input list is empty, return None
    if not value_list:
        return None
    # Initialize the head node of the linked list
    head_node = ListNode(value_list[0])
    current_node = head_node  # Pointer to the current node
    index = 1  # Index for traversing the value_list
    
    # Use a while loop to create the linked list
    while index < len(value_list):
        # Create a new ListNode for the next value
        current_node.next = ListNode(value_list[index])
        current_node = current_node.next  # Move to the next node
        index += 1  # Increment index to process the next value
    
    return head_node  # Return the head of the linked list

# Helper function to convert linked list to a list for easy display
def linked_list_to_list(head_node):
    result_list = []  # Initialize an empty list to store values
    current_node = head_node  # Pointer to traverse the linked list
    
    # Use a while loop to traverse the linked list
    while current_node:
        result_list.append(current_node.val)  # Append the current node's value to result_list
        current_node = current_node.next  # Move to the next node
    
    return result_list  # Return the resulting list

# Example usage
# head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
# new_head = removeElements(head, 6)
# print(linked_list_to_list(new_head))  # Output: [1, 2, 3, 4, 5]

# empty_head = create_linked_list([])
# new_empty_head = removeElements(empty_head, 1)
# print(linked_list_to_list(new_empty_head))  # Output: []

# head2 = create_linked_list([7, 7, 7, 7])
# new_head2 = removeElements(head2, 7)
# print(linked_list_to_list(new_head2))  # Output: []
