# Remove Dups: Wrie cod to remove duplicates from an unsorted linked list
# Follow-up
# How would you solve this problem if a temporary buffer is not allowed

class Node:
    # Constructor
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None

    # Insert a new node to the end of the linked list
    def insert(self,data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
