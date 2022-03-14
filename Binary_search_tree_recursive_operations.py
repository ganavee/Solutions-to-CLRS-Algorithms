class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_recursive(self, data):
        if(self.root == None):
            self.root = Node(data)
            return
        self.insert_data_recursive(data, self.root)

    def insert_data_recursive(self, data, curr):
        if(data < curr.data):
            if(curr.left is None):
                curr.left = Node(data)
            else:
                self.insert_data_recursive(data, curr.left)
        else:
            if(curr.right is None):
                curr.right = Node(data)
            else:
                self.insert_data_recursive(data, curr.right)

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
    

    def display_inorder_recursive(self):
        print("In-Order Traversal")
        self.display_data_inorder_recursive(self.root)
        print()
    
    def display_data_inorder_recursive(self, curr):
        if(curr == None):
            return
        self.display_data_inorder_recursive(curr.left)
        print("{0}-->".format(curr.data), end = "")
        self.display_data_inorder_recursive(curr.right)

    def display_postorder_recursive(self):
        print("Post-Order Traversal")
        self.display_data_postorder_recursive(self.root)
        print()

    def display_data_postorder_recursive(self, curr):
        if(curr == None):
            return None
        self.display_data_postorder_recursive(curr.left)
        self.display_data_postorder_recursive(curr.right)
        print("{0}-->".format(curr.data), end = "")

    def display_preorder_recursive(self):
        print("Pre-Order Traversal")
        self.display_data_preorder_recursive(self.root)
        print()

    def display_data_preorder_recursive(self, curr):
        if(curr ==  None):
            return None
        print("{0}-->".format(curr.data), end = "")
        self.display_data_preorder_recursive(curr.left)
        self.display_data_preorder_recursive(curr.right)

    def maximum_data_recursive(self, curr):
        if(curr.right != None):
            return self.maximum_data_recursive(curr.right)
        else:
            return curr.data

    def maximum_recursive(self):
        print("Maximum element is ", self.maximum_data_recursive(self.root))

    def minimum_recursive(self):
         print("Minimum element is ", self.minimum_data_recursive(self.root))

    def minimum_data_recursive(self, curr):
        if(curr.left != None):
            return self.minimum_data_recursive(curr.left)
        else:
            return curr.data

obj = BinarySearchTree()
obj.insert_recursive(16)
obj.insert_recursive(10)
obj.insert_recursive(15)
obj.insert_recursive(21)
obj.insert_recursive(7)
obj.insert_recursive(23)
obj.insert_recursive(27)
obj.insert_recursive(13)
obj.insert_recursive(14)
obj.insert_recursive(18)
obj.insert_recursive(25)
obj.insert_recursive(17)
obj.insert_recursive(8)
obj.display_inorder_recursive()
obj.display_postorder_recursive()
obj.display_preorder_recursive()
obj.maximum_recursive()
obj.minimum_recursive()
