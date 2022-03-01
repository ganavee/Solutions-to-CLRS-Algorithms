#Implement the dictionary operations INSERT, DELETE,
#and SEARCH using singly linked, circular lists. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, elem):
        node = Node(elem)
        if(self.head == None):
            self.head = node
            return
        node.next = self.head
        self.head = node

    def delete(self, elem):
        #first_element
        if(self.head.data == elem):
            self.head = self.head.next
            return
        #middle_element #last_element
        curr = prev = self.head
        while(curr and curr.data != elem):
            prev = curr
            curr = curr.next
        if(curr == None):
            print("Element not found")
            return
        prev.next = curr.next
                

    def search(self, elem):
        curr = self.head
        while(curr and curr.data != elem):
            curr = curr.next
        if(curr):
            print("Element {0} found".format(elem))
            return
        print("Element {0} not found".format(elem))

    def display(self):
        curr = self.head
        while(curr):
            print("{0}-->".format(curr.data), end = "")
            curr = curr.next
        print()
        

obj = LinkedList()
obj.insert(25)
obj.display()
obj.insert(36)
obj.display()
obj.delete(25)
obj.display()
obj.insert(98)
obj.display()
obj.search(25)
obj.search(36)
