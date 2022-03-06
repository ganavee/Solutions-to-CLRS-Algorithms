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
