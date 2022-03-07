class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if(self.root == None):
            self.root = Node(data)
            return
        self.insert_data(data, self.root)

    def insert_data(self, data, curr):
        if(data < curr.data):
            if(curr.left is None):
                curr.left = Node(data)
            else:
                self.insert_data(data, curr.left)
        else:
            if(curr.right is None):
                curr.right = Node(data)
            else:
                self.insert_data(data, curr.right)

    def search_data_recursive(self, data, curr):
        if(curr == None):
            return None
        elif(data == curr.data):
            return True
        elif(data < curr.data):
            return self.search_data_recursive(data, curr.left)
        elif(data >= curr.data):
            return self.search_data_recursive(data, curr.right)

    def search_recursive(self, data):
        if(self.root == None):
            print("No nodes present hence the element  {0} not present".format(data))
            return
        if(self.search_data_recursive(data, self.root)):
            print("Element {0} Found".format(data))
        else:
             print("Element {0} Not Found".format(data))

    def search_iterative(self, data):
        curr = self.root
        while(curr):
            if(curr.data == data):
                print("Element {0} Found".format(data))
                break
            elif(data < curr.data):
                curr = curr.left
            else:
                curr = curr.right
        if(curr == None):
            print("Element {0} Not Found".format(data))

    def minimum(self):
        curr = self.root
        while(curr):
            if(curr.left == None):
                print("Minimum element is ", curr.data)
                break
            curr = curr.left

    def maximum(self):
        curr = self.root
        while(curr):
            if(curr.right == None):
                print("Maximum element is ", curr.data)
                break
            curr = curr.right

    def display(self):
        self.display_data(self.root)
        print()
    
    def display_data(self, curr):
        if(curr == None):
            return
        self.display_data(curr.left)
        print("{0}-->".format(curr.data), end = "")
        self.display_data(curr.right)


obj = BinarySearchTree()
obj.insert(6)
obj.display()
obj.insert(2)
obj.display()
obj.insert(7)
obj.display()
obj.insert(5)
obj.display()
obj.insert(1)
obj.display()
obj.insert(3)
obj.display()
obj.insert(4)
obj.display()
obj.insert(10)
obj.display()
obj.insert(6)
obj.display()
obj.minimum()
obj.maximum()
obj.search_iterative(1)
obj.search_iterative(8)
obj.search_recursive(2)
obj.search_recursive(8)
'''
