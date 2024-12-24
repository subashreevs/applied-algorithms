class Node:
    def _init_(self, val):
        self.val = val
        self.next = None

class Queue_LL:
    def _init_(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, val:int)->None:
        newNode=Node(val)
        if self.tail is None:
            self.tail=newNode
            self.head=newNode
        else:    
            self.tail.next=newNode
            self.tail=newNode
    
    def dequeue(self)->int:
        if self.head is None:
            return
        
        self.head=self.head.next

        if self.head is None:
            self.tail = None

    def QueueToList(self)->list[int]:
        if self.head is None:
            return []
        
        now=self.head
        arrayQ=[]
        while now:
            arrayQ.append(now.val)
            now=now.next

        return arrayQ
    
# #Test    
# conveyor_belt = Queue_LL()

# # Test input 1:
# operations = [["enqueue", 1], ["enqueue", 2], ["enqueue", 3], ["dequeue"],
#               ["enqueue", 4], ["dequeue"], ["dequeue"], ["enqueue", 6]]

# # Execute operations:
# for op in operations:
#     if op[0] == "enqueue":
#         conveyor_belt.enqueue(op[1])
#     elif op[0] == "dequeue":
#         print(f"Dequeued: {conveyor_belt.dequeue()}")

# # Convert the queue to a list and display the final state
# print("Final queue:", conveyor_belt.QueueToList())