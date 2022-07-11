import sys
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Singly_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

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
        temp = self.head
        while(temp.next != None):
            prev = temp
            temp = temp.next
        prev.next = None
        self.tail = prev
        self.count -= 1

    def delete_pos(self):
        if(self.count == 0):
            print("No nodes to delete")
            return
        print("Enter position")
        pos = int(sys.stdin.readline().strip())
        if(self.count == 1 and pos == 1):
            self.head = None
            self.tail = None
            self.count -= 1
            return
        if(pos > self.count):
            print("Position out of range")
            return
        if(pos == 1):
            self.delete_first()
            return
        if(pos == self.count):
            self.delete_last()
            return
        counter = 1
        temp = self.head
        while(counter < pos):
            prev = temp
            temp = temp.next
            counter += 1
        prev.next = temp.next
        self.count -= 1

    def delete_value(self):
        if(self.count == 0):
            print("No nodes to delete")
            return
        print("Enter value")
        value = int(sys.stdin.readline().strip())
        if(self.count == 1 and self.head.val == value):
            self.head = None
            self.tail = None
            self.count -= 1
            return
        temp = self.head
        counter = 1
        while(temp and temp.val != value):
            counter += 1
            prev = temp
            temp = temp.next
        if(counter == 1):
            self.delete_first()
        elif(counter == self.count):
            self.delete_last()
        elif(counter > self.count):
            print("Value not present")
            return
        else:
            prev.next = temp.next
            self.count -= 1
            
        
        
    def insert(self, value, pos):
        if(pos == 1):
            self.insert_first(value)
        elif(pos > self.count):
            self.insert_last(value)
        else:
            if(self.head == None):
                self.head = Node(value)
                self.tail = self.head
                self.count += 1
                return
            counter = 1
            temp = self.head
            while(counter < pos-1):
                temp = temp.next
                counter += 1
            node = Node(value)
            node.next = temp.next
            temp.next = node
            self.count += 1

    def insert_last(self, value):
        if(self.head == None):
            self.head = Node(value)
            self.tail = self.head
            self.count += 1
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.count += 1

    def insert_first(self, value):
        if(self.head == None):
            self.head = Node(value)
            self.tail = self.head
            self.count += 1
            return
        node = Node(value)
        node.next = self.head
        self.head = node
        self.count += 1
        

    def display(self):
        next_pointer = self.head
        while(next_pointer != None):
            print("{0}-->".format(next_pointer.val), end = "")
            next_pointer = next_pointer.next
        print("END")
        print("Number of nodes = ", obj.count)
        

obj = Singly_list()
while(True):
    print("Enter \n1. To Terminate\n2. To Enter data \n3. To Delete\n4. To Display")
    val = sys.stdin.readline().strip()
    if(val == "1"):
        break
    elif(val == "2"):
        print("Enter \n1. To Insert First\n2. To Insert Last\n3. To Insert at Position ")
        pos = sys.stdin.readline().strip()
        print("Enter Value")
        data = int(sys.stdin.readline().strip())
        if(pos == "1"):
            obj.insert_first(data)
        elif(pos == "2"):
            obj.insert_last(data)
        elif(pos == "3"):
            print("Enter position")
            pos = int(sys.stdin.readline().strip())
            obj.insert(data, pos)
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
        obj.display()
    else:
        print("Please enter valid Number")

print("END OF PROGRAM")
#obj.display()

