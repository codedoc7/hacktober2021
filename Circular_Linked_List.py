# circular linked list traversal

# Structure for a Node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1  # For the first node

        self.head = ptr1

    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break


# Initialize list as empty
cllist = CircularLinkedList()

cllist.push(86)
cllist.push(13)
cllist.push(40)
cllist.push(34)
cllist.push(12)

print("Contents of circular Linked List: ")
cllist.printList()
# Created linked list will be 12->34->40->13->86
