# Remove Dups: Write code to remove duplicates from an unsorted linked list
# Follow-up
# How would you solve this problem if a temporary buffer is not allowed

# Thoughts on the solution
# 1. Need to implement a linked list using appropriate classes.
# 2. Manually create a random unsorted linked list with duplicates
# 3. Create a function that given a linked list as an input, deletes the duplicates
# 4. A brute force approach for the function would be to send a runner function across the length of the linked list for each node to delete the duplicates
# 

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
    
    def removeDuplicates(self):
        if(self.head):
            current = self.head
            current2 = self.head
            dataValue = current.data
            while(current.next):
                while(current2.next): # For each value, iterate through the entire linked list to remove its duplicates
                    if current2.next.data == dataValue:
                        current2.next = current2.next.next #Remove the node under examination from the linked list by removing its linkage
                    current2 = current2.next
                    if(current2 == None):
                        break
                current = current.next
                current2 = current.next
                dataValue = current.data

    def printValues(self):
        if(self.head):
            current = self.head
            print(current.data)
            while(current.next):
                current = current.next
                print(current.data)
                

testList = LinkedList()


testList.insert('a')
testList.insert('d')
testList.insert('b')
testList.insert('x')
testList.insert('a')
testList.insert('g')
testList.insert('x')
testList.insert('i')
testList.insert('x')
testList.insert('g')
testList.insert('a')

print("-----------------------------")
testList.printValues()
testList.removeDuplicates()
print("---------------------------------")
testList.printValues()