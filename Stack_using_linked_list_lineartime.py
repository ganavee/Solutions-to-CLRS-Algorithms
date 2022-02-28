#Implementing Stack using Singly Linked List.
#The operations PUSH and POP still take O(1) time.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node
        

    def pop(self):
        if(self.head == None):
            print("No elements to pop")
            return
        self.head = self.head.next
        
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
