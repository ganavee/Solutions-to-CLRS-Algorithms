class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, data):
        if(self.root == None):
            self.root = Node(data)
            self.display_inorder_recursive()
            return
        curr = self.root
        while(curr):
            prev = curr
            if(data < curr.data):
                curr = curr.left
                left = 1
            else:
                curr = curr.right
                left = 0
        if(left == 1):
            prev.left = Node(data)
        else:
            prev.right = Node(data)
        self.display_inorder_recursive()
        
    def display_inorder_recursive(self):
        #print("In-Order Traversal")
        self.display_data_inorder_recursive(self.root)
        #print()
    
    def display_data_inorder_recursive(self, curr):
        if(curr == None):
            return
        self.display_data_inorder_recursive(curr.left)
        #print("{0}-->".format(curr.data), end = "")
        self.display_data_inorder_recursive(curr.right)

    def display_inorder_iterative(self):
        print("Iterative In-Order Traversal")
        curr = self.root
        stack = []
        #using one loop
        while True:
            if(curr != None):
                stack.append(curr)
                curr = curr.left
            elif(len(stack)):
                curr = stack.pop()
                print("{0}-->".format(curr.data), end = "")
                curr = curr.right
                
        #using two loops
        '''
        stack = [None]
        while(len(stack) != 0 or curr):
            #print("length of stack ", len(stack))
            while True:
                stack.append(curr)
                #print("Appending curr ", curr.data)
                if(curr.left == None):
                    break
                curr = curr.left
            curr = stack.pop()
            #print("curr = ", curr.data)
            print("{0}-->".format(curr.data), end = "")
            while(curr and curr.right == None):
                curr = stack.pop()
                if(curr != None):
                    print("{0}-->".format(curr.data), end = "")
            if(curr and curr.right != None):
                curr = curr.right
        '''
            
        

obj = Binary_Search_Tree()
obj.insert_iterative(16)
obj.insert_iterative(10)
obj.insert_iterative(21)
obj.insert_iterative(23)
obj.insert_iterative(18)
obj.insert_iterative(15)
obj.insert_iterative(7)
obj.insert_iterative(27)
obj.insert_iterative(13)
obj.insert_iterative(14)
obj.insert_iterative(25)
obj.insert_iterative(17)
obj.display_inorder_iterative()

