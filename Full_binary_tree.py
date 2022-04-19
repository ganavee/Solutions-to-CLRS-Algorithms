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

    def full_binary_tree(self):
        curr = self.head
        queue = [curr]
        flag = False
        level = 0
        total_level_nodes = 2**level
        node_count = 0
        none_node = 0
        while(len(queue)):
            curr = queue.pop(0)
            node_count += 1
            if(curr != None):
                if(flag == True):
                    print("The given tree is not Full binary tree")
                    return
                self.heap.append(curr.data)
                if(curr.left == None and curr.right != None):
                    print("The given tree is not Full binary tree")
                    return
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                self.heap.append('-')
                flag = True
                none_node += 1
            if(node_count == total_level_nodes):
                if(none_node == total_level_nodes):
                    print("The given tree is Full binary tree")
                    return
                level += 1
                total_level_nodes = 2**level
                node_count = 0
        

obj = Tree()

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
'''
obj.inorder_traversal()
obj.full_binary_tree()
