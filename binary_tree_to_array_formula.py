class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None


    def insert(self, data):
        if(self.head == None):
            self.head = Node(data)
            return
        curr = self.head
        while(True):
            if(data > curr.data):
                if(curr.right != None):
                    curr = curr.right
                else:
                    curr.right = Node(data)
                    break
            else:
                if(curr.left != None):
                    curr = curr.left
                else:
                    curr.left = Node(data)
                    break

    def inorder_traversal(self):
        curr = self.head
        inorder = []
        stack = []
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
        print("Inorder Traversal ", inorder)

    def print_heap(self):
        curr = self.head
        queue = [curr]
        heap = []
        level = 0
        level_nodes = 2**level
        nodes_count = 0
        none_nodes = 0
        while(len(queue)):
            curr = queue.pop(0)
            nodes_count += 1
            if(curr == None):
                none_nodes += 1
                heap.append('-')
                queue.append(None)
                queue.append(None)
            else:
                heap.append(curr.data)
                #if(curr.left != None or curr.right != None):
                queue.append(curr.left)
                queue.append(curr.right)
            if(nodes_count == level_nodes):
                if(none_nodes == level_nodes):
                    break
                level += 1
                nodes_count = 0
                level_nodes = 2**level
                none_nodes = 0
        while(True):
            if(heap[-1] == '-'):
                heap.pop()
            else:
                break
        print("Heap representation of tree ", heap)

obj = Tree()
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
obj.print_heap()


