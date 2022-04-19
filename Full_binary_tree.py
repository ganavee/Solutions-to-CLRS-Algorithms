class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
        self.heap = []

    def insert(self, data):
        curr = self.head
        if(self.head == None):
            self.head = Node(data)
            return
        while(True):
            if(data > curr.data):
                if(curr.right == None):
                    curr.right = Node(data)
                    break
                else:
                    curr = curr.right
            else:
                if(curr.left == None):
                    curr.left = Node(data)
                    break
                else:
                    curr = curr.left

    def is_complete_binary_tree(self):
        level = 0
        total_level_nodes = 2 ** level
        node_count = 0
        curr = self.head
        queue = [curr]
        none_nodes = 0
        flag = False
        while(len(queue)):
            curr = queue.pop(0)
            node_count += 1
            if(curr != None):
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                none_nodes += 1
            if(node_count == total_level_nodes):
                print("level", level)
                if(none_nodes != 0):
                    if(none_nodes != total_level_nodes):
                        print("The given Tree is not a Complete Binary Tree")
                        flag = True
                    break
                level += 1
                node_count = 0
                none_nodes = 0
                total_level_nodes = 2 ** level
        if(flag == False):
            print("The given Tree is a Complete Binary Tree")

    def inorder_traversal(self):
        curr = self.head
        stack = []
        inorder = []
        while(True):
            if(curr != None):
                stack.append(curr)
                curr = curr.left
            elif(len(stack)):
                curr = stack.pop()
                inorder.append(curr.data)
                curr = curr.right
            else:
                break
        print("Inorder Traversal is ", inorder)

obj = Tree()
'''
obj.insert(16)
obj.insert(10)
obj.insert(21)
obj.insert(15)
obj.insert(18)
obj.insert(23)
obj.insert(7)
'''
obj.insert(16)
obj.insert(10)
obj.insert(7)
obj.insert(21)
obj.insert(8)
obj.insert(15)
obj.insert(13)
obj.insert(23)
obj.insert(25)
obj.insert(24)
obj.insert(14)

obj.inorder_traversal()
obj.is_complete_binary_tree()
