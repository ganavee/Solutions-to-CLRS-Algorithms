import sys
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
        


class Doubly_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_first(self, data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
            self.count += 1
            return
        node = Node(data)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.count += 1

    def insert_last(self, data):
        if(self.count == 0):
            self.insert_first(data)
            return
        node = Node(data)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.count += 1

    def insert_pos(self, data, pos):
        if(self.count == 0):
            self.insert_first(data)
            return
        if(pos == 1):
            self.insert_first(data)
            return
        if(pos == self.count+1):
            self.insert_last(data)
            return
        counter = 1
        temp = self.head
        while(counter < pos):
            prev = temp
            temp = temp.next
            counter += 1
        node = Node(data)
        prev.next = node
        node.prev = prev
        node.next = temp
        temp.prev = node
        self.count += 1

    def display(self):
        temp = self.head
        while(temp != None):
            print("{0}-->".format(temp.val), end ="")
            temp = temp.next
        print("END")
        print("Number of Nodes ", self.count)

    def delete_first(self):
        if(self.count == 0):
            print("No nodes to delete")
            return
        if(self.count == 1):
            self.head = None
            self.tail = None
            self.count -= 1
            return
        self.head = self.head.next
        self.head.prev = None
        self.count -= 1

    def delete_last(self):
        if(self.count == 0):
            print("No nodes to delete")
            return
        if(self.count == 1):
            self.head = None
            self.tail = None
            self.count -= 1
            return
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.count -= 1

    def delete_pos(self):
        if(self.count == 0):
            print("No nodes to delete")
            return
        print("Enter position")
        pos = int(sys.stdin.readline().strip())
        if(pos == 1):
            self.delete_first()
            return
        if(pos == self.count):
            self.delete_last()
            return
        if(pos > self.count):
            print("Only {0} nodes present, please enter valid option".format(self.count))
            return
        counter = 1
        while(counter < pos):
            prev = temp
            temp = temp.next
            counter += 1
        prev.next = temp.next
        temp.next.prev = prev
        self.count -= 1

    def delete_value(self):
        if(self.count == 0):
            print("No nodes to delete")
            return
        print("Enter Value")
        data = int(sys.stdin.readline().strip())
        if(self.count == 1 and data == self.head.val):
            self.head = None
            self.tail = None
            self.count -= 1
            return
        temp = self.head
        counter = 0
        while(temp and temp.val != data):
            temp = temp.next
            counter += 1
        if(temp == None):
            print("Node with value {0} not found".format(data))
        elif(counter == 1):
            self.delete_first()
            return
        elif(counter == self.count):
            self.delete_last()
            return
        else:
            self.delete_pos(counter+1)
            return

    def display_reverse(self):
        temp = self.tail
        while(temp != None):
            print("{0}-->".format(temp.val), end ="")
            temp = temp.prev
        print("START")
        print("Total number of nodes  = ", self.count)


obj = Doubly_list()
while(True):
    print("Enter \n1. To Terminate\n2. To Enter data \n3. To Delete\n4. To Display")
    val = sys.stdin.readline().strip()
    if(val == "1"):
        break
    elif(val == "2"):
        print("Enter \n1. To Insert First\n2. To Insert Last\n3. To Insert at Position ")
        option = sys.stdin.readline().strip()
        print("Enter Value")
        data = int(sys.stdin.readline().strip())
        if(option == "1"):
            obj.insert_first(data)
        elif(option == "2"):
            obj.insert_last(data)
        elif(option == "3"):
            print("Enter position")
            pos = int(sys.stdin.readline().strip())
            obj.insert_pos(data, pos)
        else:
            print("Enter Valid number")
        obj.display()
    elif(val == "3"):
        print("Enter \n1. To Delete First\n2. To Delete Last\n3. To Delete at Position\n4. To Delete value ")
        remove = sys.stdin.readline().strip()
        if(remove == "1"):
            obj.delete_first()
        elif(remove == "2"):
            obj.delete_last()
        elif(remove == "3"):
            obj.delete_pos()
        elif(remove == "4"):
            obj.delete_value()
        else:
            print("Enter Valid Number")
        obj.display()
    elif(val == "4"):
        print("Enter \n1. To Print first to last \n2. To Print reverse order")
        option = sys.stdin.readline().strip()
        if(option == "1"):
            obj.display()
        elif(option == "2"):
            obj.display_reverse()
        else:
            print("Please send valid option")
        
    else:
        print("Please enter valid Number")

print("END OF PROGRAM")
