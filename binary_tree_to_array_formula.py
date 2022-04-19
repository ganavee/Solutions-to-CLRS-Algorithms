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
        while(len(queue)):
            curr = queue.pop(0)
            if(curr == None):
                heap.append('-')
            else:
                heap.append(curr.data)
                if(curr.left != None or curr.right != None):
                    queue.append(curr.left)
                    queue.append(curr.right)
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


