import sys
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Singly_list_recursion:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_recursive_pos(self, data, temp, pos, current_pos):
        if(pos < 1 or pos > (self.count+1)):
            print("Please enter valid positions between 1 and {0}".format(self.count+1))
            return
        if(pos == 1):
            node = Node(data)
            node.next = self.head
            self.head = node
            self.count += 1
            return
            
        if(current_pos == pos-1):
            node = Node(data)
            node.next = temp.next
            temp.next = node
            self.count += 1
            return
        return self.insert_recursive_pos(data, temp.next, pos, current_pos+1)
        

    def insert_pos(self, data, pos):
        temp = self.head
        self.insert_recursive_pos(data, self.head, pos, 1)
        self.display()

    def insert_recursive(self, data, temp):
        if(self.head == None):
            self.head = Node(data)
            return
        if(temp.next == None):
            temp.next = Node(data)
            return
        return self.insert_recursive(data, temp.next)

    def insert(self, data):
        temp = self.head
        self.insert_recursive(data, self.head)
        self.display()

    def display(self):
        temp = self.head
        while(temp != None):
            print("{0}-->".format(temp.val), end = "")
            temp = temp.next
        print("END")
        print("Total number of nodes ", self.count)

    def insert_Rec(self, val, index, node):
        if(index == 0):
            temp = Node(val)
            self.count += 1
            temp.next = node
            return temp
        node.next = self.insert_Rec(val, index-1, node.next)
        return node

    def kunal_insert(self, val, index):
        self.head = self.insert_Rec(val, index, self.head)
        self.display()


obj = Singly_list_recursion()
'''
obj.insert_pos(10, 1)
obj.insert_pos(11, 1)
obj.insert_pos(12, 1)
obj.insert_pos(13, 2)
obj.insert_pos(14, 4)
obj.insert_pos(15, 6)
obj.insert_pos(16, 0)
obj.insert_pos(18, 7)
'''
obj.kunal_insert(10,0)
obj.kunal_insert(11,1)
obj.kunal_insert(12,2)
obj.kunal_insert(13,3)
obj.kunal_insert(14,2)
