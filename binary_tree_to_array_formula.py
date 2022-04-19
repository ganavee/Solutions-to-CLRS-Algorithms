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
        level = 0
        level_nodes = 2**level
        nodes_count = 0
        none_nodes = 0
        while(len(queue)):
            curr = queue.pop(0)
            nodes_count += 1
            if(curr == None):
                none_nodes += 1
                self.heap.append('-')
                queue.append(None)
                queue.append(None)
            else:
                self.heap.append(curr.data)
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
        '''
        while(True):
            if(self.heap[-1] == '-'):
                self.heap.pop()
            else:
                break
        '''
        print("Heap representation of tree ", self.heap)

    def find_leftchild(self, elem):
        for i in range(len(self.heap)):
            if(elem == self.heap[i]):
                left_child = self.heap[2*i + 1]
                if(left_child == '-'):
                    print("Left Child of {0} is not present".format(elem))
                else:
                    print("Left child of {0} is {1}".format(elem, left_child))
                break
        else:
            print("Element {0} is not present".format(elem))

    def find_rightchild(self, elem):
        for i in range(len(self.heap)):
            if(elem == self.heap[i]):
                right_child = self.heap[2*i + 2]
                if(right_child == '-'):
                    print("Right child of {0} is not present".format(elem))
                else:
                    print("Right child of {0} is {1}".format(elem, right_child))
                break
        else:
            print("Element {0} not present".format(elem))

    def find_parent(self, elem):
        for i in range(len(self.heap)):
            if(elem == self.heap[i]):
                if(i%2 == 0):
                    parent = self.heap[i//2 - 1]
                else:
                    parent = self.heap[i//2]
                print("Parent of {0} is {1}".format(elem, parent))
                break
        else:
            print("Element {0} not present".format(elem))

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
obj.find_leftchild(21)
obj.find_rightchild(10)
obj.find_parent(29)


