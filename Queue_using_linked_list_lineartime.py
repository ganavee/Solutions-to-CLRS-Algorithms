#Implement a queue by a singly linked list LL.
#The operations ENQUEUE and DEQUEUE should still take O(1) time.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.curr = None

    def enqueue(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = self.curr = node
        else:
            self.curr.next = node
            self.curr = node

    def dequeue(self):
        if(self.head == None):
            print("Queue is empty")
            return
        self.head = self.head.next

    def display(self):
        itr = self.head
        if(itr == None):
            print("No elements in Queue")
        while(itr):
            print("{0}-->".format(itr.data), end = "")
            itr = itr.next
        print()

obj = LinkedList()
obj.enqueue(25)
obj.display()

obj.enqueue(30)
obj.display()
obj.dequeue()
obj.display()
obj.dequeue()
obj.display()

obj.dequeue()
obj.display()

obj.enqueue(55)
obj.display()

