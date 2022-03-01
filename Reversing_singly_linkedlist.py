'''
Give a Θ(n)-time nonrecursive procedure that reverses a singly linked list of
n elements. The procedure should use no more than constant storage
beyond that needed for the list itself.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if(self.head == None):
            self.head = node
            print("After insertion")
            self.display()
            return
        node.next = self.head
        self.head = node
        print("After insertion")
        self.display()

    def reverse(self):
        if(self.head == None): #if(!self.head)
            print("No elements to reverse")
            return
        if(self.head.next == None): #if(!self.head)
            print("Single element hence nothing to reverse")
            return
        prev = self.head
        curr = self.head.next
        prev.next = None
        temp = curr.next
        while(temp):
            curr.next = prev
            prev = curr
            curr = temp
            temp = curr.next
        curr.next = prev
        self.head = curr
        print("Reversed elements are ")
        self.display()

    def display(self):
        itr = self.head
        while(itr):
            print("{0}-->".format(itr.data), end = "")
            itr = itr.next
        print()

obj = LinkedList()
obj.insert(10)
obj.insert(30)
obj.insert(70)
obj.insert(90)
obj.insert(20)
obj.reverse()
obj.reverse()

