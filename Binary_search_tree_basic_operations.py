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


    def display_inorder(self):
        print("In-Order Traversal")
        self.display_data_inorder(self.root)
        print()
    
    def display_data_inorder(self, curr):
        if(curr == None):
            return
        self.display_data_inorder(curr.left)
        print("{0}-->".format(curr.data), end = "")
        self.display_data_inorder(curr.right)  

    def display_postorder(self):
        print("Post-Order Traversal")
        self.display_data_postorder(self.root)
        print()

    def display_data_postorder(self, curr):
        if(curr == None):
            return None
        self.display_data_postorder(curr.left)
        self.display_data_postorder(curr.right)
        print("{0}-->".format(curr.data), end = "")

    def display_preorder(self):
        print("Pre-Order Traversal")
        self.display_data_preorder(self.root)
        print()

    def display_data_preorder(self, curr):
        if(curr ==  None):
            return None
        print("{0}-->".format(curr.data), end = "")
        self.display_data_preorder(curr.left)
        self.display_data_preorder(curr.right)








        

obj = BinarySearchTree()
obj.insert(16)
obj.display_inorder()
obj.insert(10)
obj.display_inorder()
obj.insert(15)
obj.display_inorder()
obj.insert(21)
obj.display_inorder()
obj.insert(7)
obj.display_inorder()
obj.insert(23)
obj.display_inorder()
obj.insert(27)
obj.display_inorder()
obj.insert(13)
obj.display_inorder()
obj.insert(14)
obj.display_inorder()
obj.insert(18)
obj.display_inorder()
obj.insert(25)
obj.display_inorder()
obj.insert(17)
obj.display_inorder()
obj.display_postorder()
obj.display_preorder()
'''
obj.minimum()
obj.maximum()
obj.search_iterative(1)
obj.search_iterative(8)
obj.search_recursive(2)
obj.search_recursive(8)
'''
