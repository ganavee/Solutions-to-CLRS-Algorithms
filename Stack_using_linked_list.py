#Implementing Stack using Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        itr = self.head
        if(itr == None):
            self.head = node
        else:
            prev = self.head
            while(itr):
                prev = itr
                itr = itr.next
            prev.next = node

    def pop(self):
        if(self.head == None):
            print("No elements to pop")
            return
        prev = self.head
        itr = self.head
        while(itr.next):
            prev = itr
            itr = itr.next
        prev.next = None

    def display(self):
        itr = self.head
        while(itr):
            print("{0}-->".format(itr.data), end = "")
            itr = itr.next
        print()

obj = LinkedList()
obj.push(25)
obj.display()
obj.push(30)
obj.display()
obj.pop()
obj.display()
