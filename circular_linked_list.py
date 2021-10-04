class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def insertAtBeg(self, data):
        newNode = Node(data)
        if self.last == None:
            self.last = newNode
            self.last.next = newNode
            return

        newNode.next = self.last.next
        self.last.next = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.last == None:
            self.last = newNode
            self.last.next = newNode
            return

        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode

    def insertAtMiddle(self, position, data):
        new_node = Node(data)
        temp = self.last.next
        for i in range(position - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def deleteFromBeg(self):
        self.last.next = self.last.next.next

    def deleteFromLast(self):
        temp = self.last.next
        while temp:
            temp = temp.next
            if temp.next == self.last:
                break
        temp.next = self.last.next
        self.last = temp

    def deleteFromMiddle(self, position):
        temp = self.last.next
        for _ in range(position-1):
            temp = temp.next

        temp.next = temp.next.next

    def display(self):
        temp = self.last.next
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
            if temp == self.last.next:
                break

cll = CircularLinkedList()

while True:
    print("\n1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at middle")
    print("4. Delete from beginning")
    print("5. Delete from end")
    print("6. Delete from middle")
    print("7. Display")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the data: "))
        cll.insertAtBeg(data)
    elif choice == 2:
        data = int(input("Enter the data: "))
        cll.insertAtEnd(data)
    elif choice == 3:
        data = int(input("Enter the data: "))
        position = int(input("Enter the position: "))
        cll.insertAtMiddle(position, data)
    elif choice == 4:
        cll.deleteFromBeg()
    elif choice == 5:
        cll.deleteFromLast()
    elif choice == 6:
        position = int(input("Enter the position: "))
        cll.deleteFromMiddle(position)
    elif choice == 7:
        cll.display()
    elif choice == 8:
        break