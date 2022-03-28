class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = 0

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, data):
        if(self.root == None):
            self.root = Node(data)
            #self.display_inorder_iterative()
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
        #self.display_inorder_iterative()

    
    def display_preorder_iterative(self):
        print("Iteratice Pre-Order Traversal")
        stack = [None]
        curr = self.root
        while(curr != None and len(stack) != 0):
            if(curr.visited == 0):
                print("{0}-->".format(curr.data), end = "")
                curr.visited = 1
                stack.append(curr)
            if(curr.left != None and curr.left.visited == 0):
                curr = curr.left
            elif(curr.right != None and curr.right.visited == 0):
                curr = curr.right
            else:
                curr = stack.pop()
        print()
        print()
        

    def display_postorder_iterative(self):
        print("Iterative Post-Order Traversal")
        stack = [None]
        curr = self.root
        while(curr != None or len(stack) != 0):
            while(curr.left != None and curr.left.visited == 0):
                stack.append(curr)
                curr = curr.left
            if(curr.right != None and curr.right.visited == 0):
                stack.append(curr)
                curr = curr.right
            else:
                print("{0}-->".format(curr.data), end = "")
                curr.visited = 1
                curr = stack.pop()
        print()
        print()

    def initialising_visit(self):
        curr = self.root
        stack = []
        #using one loop
        while True:
            if(curr != None):
                stack.append(curr)
                curr = curr.left
            elif(len(stack)):
                curr = stack.pop()
                #print("{0}-->".format(curr.data), end = "")
                curr.visited = 0
                curr = curr.right
            else:
                break
        
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
            else:
                break
        print()
        print()
                
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

    def inorder_predecessor(self, elem):
        prev = None
        curr = self.root
        stack = []
        while(True):
            if(curr != None):
                stack.append(curr)
                curr = curr.left
            elif(len(stack) != 0):
                curr = stack.pop()
                if(curr.data ==  elem):
                    if(prev != None):
                        print("Inorder Predecessor of {0} is {1}".format(elem, prev.data))
                    else:
                        print("Inorder Predecessor of {0} is Not Present".format(elem))
                    break
                prev = curr
                curr = curr.right
            else:
                print("Inorder Predecessor of {0} is Not Present".format(elem))
                break

    def postorder_predecessor(self, elem):
        curr = self.root
        prev = None
        nextt = None
        stack = [curr]
        while(len(stack)):
            curr = stack.pop()
            if(curr):
                if(prev == elem):
                    print("Postorder Predecessor of {0} is {1}".format(elem, curr.data))
                    break
                prev = curr.data
                stack.append(curr.left)
                stack.append(curr.right)
        if(curr == None):
            print("Postorder Predecessor of {0} is {1}".format(elem, curr))

    def preorder_predecessor(self, elem):
        curr = self.root
        prev = None
        stack = [curr]
        while(len(stack)):
            curr = stack.pop()
            if(curr):
                if(curr.data == elem):
                    print("Preorder Predecessor of {0} is {1}".format(elem, prev))
                    break
                prev = curr.data
                stack.append(curr.right)
                stack.append(curr.left)


    def has_child(self, elem):
        curr = self.root
        parent = None
        while(curr):
            if(elem == curr.data):
                if(curr.right != None):
                    #find the sucessor and return sucessor and the right child
                    succ = self.successor(elem)
                    #print("{0} has a right child {1}".format(elem, curr.right.data))
                    return(curr.right, succ, parent, True, parent_child_direction, curr.left)
                elif(curr.left != None):
                    print("{0} has a left child {1}".format(elem, curr.left.data))
                    return(curr.left, None, parent, False, parent_child_direction, None)
                else:
                    print("{0} does not have a child".format(elem))
                    return(None, None, parent, None, parent_child_direction)
                break
            elif(elem < curr.data):
                parent = curr
                parent_child_direction = "left"
                curr = curr.left
            else:
                parent = curr
                parent_child_direction = "right"
                curr = curr.right

    def delete(self, elem):
        child_node, succ, parent, right, parent_child_direction, curr_left_child= self.has_child(elem)
        if(right == True):
            print("Node {0} has right child node as {1} its parent as {2} and successor as {3}".format(elem, child_node.data, parent.data, succ.data))
            if(succ == child_node):
                parent.right = succ
                child_node.left = curr_left_child
            else:
                pass
        elif(right == False):
            print("Node {0} has left child node as {1} and its parent as {2}".format(elem, child_node.data, parent.data))
            if(parent_child_direction == "right"):
                parent.right = child_node
            else:
                parent.left = child_node
        else:
            if(parent_child_direction == "right"):
                parent.right = child_node
            else:
                parent.left = child_node
        print("After deleting {0}".format(elem))
        self.display_inorder_iterative()

    def inorder_successor(self, elem):
        curr = self.root
        stack = []
        prev = None
        while(len(stack) or curr):
            if(curr):
                stack.append(curr)
                curr = curr.left
            elif(len(stack)):
                curr = stack.pop()
                if(prev == elem):
                    print("Inorder Successor of {0} is {1}".format(elem, curr.data))
                    break
                prev = curr.data
                curr = curr.right
        if(curr == None):
            print("Inorder Successor of {0} is Not present".format(elem))

    def postorder_successor(self, elem):
        curr = self.root
        stack = [curr]
        prev = None
        while(len(stack)):
            curr = stack.pop()
            if(curr):
                if(elem == curr.data):
                    print("Postorder Successor of {0} is {1}".format(elem, prev))
                    break
                prev = curr.data
                stack.append(curr.left)
                stack.append(curr.right)

    def preorder_successor(self, elem):
        curr = self.root
        stack = [curr]
        prev = None
        while(len(stack)):
            curr = stack.pop()
            if(curr):
                if(prev == elem):
                    print("Preorder Successor of {0} is {1}".format(elem, curr.data))
                    break
                prev = curr.data    
                stack.append(curr.right)
                stack.append(curr.left)
        if(curr ==  None):
            print("Preorder Successor of {0} is {1}".format(elem, curr))
        
        

obj = Binary_Search_Tree()
obj.insert_iterative(16)
obj.insert_iterative(10)
obj.insert_iterative(21)
obj.insert_iterative(23)
obj.insert_iterative(18)
obj.insert_iterative(15)
obj.insert_iterative(7)
obj.insert_iterative(25)
obj.insert_iterative(35)
obj.insert_iterative(13)
obj.insert_iterative(14)
obj.insert_iterative(24)
obj.insert_iterative(30)
obj.insert_iterative(29)
obj.insert_iterative(65)
obj.insert_iterative(72)
obj.insert_iterative(63)
obj.insert_iterative(26)
obj.insert_iterative(28)
obj.insert_iterative(27)
obj.insert_iterative(17)
obj.insert_iterative(8)

obj.display_postorder_iterative()
obj.postorder_predecessor(7)
obj.postorder_successor(24)
obj.initialising_visit()
obj.display_preorder_iterative()
obj.preorder_predecessor(16)
obj.preorder_successor(24)
obj.display_inorder_iterative()
obj.inorder_predecessor(7)
obj.inorder_successor(24)


#obj.delete(21)
'''
obj.has_child(27)
obj.display_postorder_iterative()
obj.initialising_visit()
obj.display_preorder_iterative()
obj.minimum()
obj.maximum()
obj.search_iterative(16)
obj.predecessor(11)
obj.successor(11)
'''

