# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x
# IMPORTANT: The partition element x can appear anywhere in the "Right partition"; it does not need to appear between the left and right partitions
# The additional spacing in the example indicates teh partition. Yes, the output below is one of many valid outputs
#
#Input 3 -> 5 -> 8 -> 5-> 10 -> 2 -> 1 (partition 5)
# Output 3 ->1 -> 2 -> 10 -> 5 -> 5 -> 8

# Thoughts on solution:
# Need to think about how to push higher values to the right and lower values to the lef
# Note that we don't know how long the linked list is
# If the value is smaller than x, then leave it where it is and move to the next item in the list
# If the value is greater than x, the traverse the length of the list until a value is discovered that is smaller than x. Then switch its position with the current node.
# Could this be done with a recursive call? I don't know, just do it conventially.

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

    def partition(self,x):
        if(self.head):
            current = self.head
            while(current.next):

            current = current.next

    def printValues(self):
        if(self.head):
            current = self.head
            print(current.data)
            while(current.next):
                current = current.next
                print(current.data)
                

testList = LinkedList()


testList.insert(1)
testList.insert(3)
testList.insert(5)
testList.insert(2)
testList.insert(7)
testList.insert(1)
testList.insert(9)
testList.insert(7)
testList.insert(2)
testList.insert(4)
testList.insert(8)

print("-----------------------------")
testList.printValues()
testList.partition(4)
print("---------------------------------")
testList.printValues()