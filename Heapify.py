class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Heap:
    def __init__(self):
        self.head = None
        self.bfs = []

    def insert(self, data):
        if(self.head == None):
            self.head = Node(data)
            return
        curr = self.head
        queue = [curr]
        curr = queue.pop()
        while(True):
            if(curr.left == None):
                curr.left = Node(data)
                break
            elif(curr.right == None):
                curr.right = Node(data)
                break
            else:
                queue.append(curr.left)
                queue.append(curr.right)
                curr = queue.pop(0)
        print("Done with inserting the element ",data)

    def bfs_tree_to_array(self):
        curr = self.head
        queue = [curr]
        while(len(queue)):
            curr = queue.pop(0)
            self.bfs.append(curr.data)
            if(curr.left != None):
                queue.append(curr.left)
            if(curr.right  !=  None):
                queue.append(curr.right)
        print()
        print("BFS ", self.bfs)

    def heapify(self):
        length = len(self.bfs)
        size  = (length // 2) - 1
        for i in range(size, -1, -1):
            parent = i
            while(True):
                left_child = 2*parent + 1
                right_child = 2*parent + 2
                if(right_child >= length):
                    if(left_child < length and self.bfs[left_child] > self.bfs[parent]):
                        swap = self.bfs[parent]
                        self.bfs[parent] = self.bfs[left_child]
                        self.bfs[left_child] = swap
                        parent = left_child
                    else:
                        break
                else:
                    if(left_child < length  and self.bfs[left_child] > self.bfs[right_child]):
                        if(self.bfs[left_child] > self.bfs[parent]):
                            swap = self.bfs[parent]
                            self.bfs[parent] = self.bfs[left_child]
                            self.bfs[left_child] = swap
                            parent = left_child
                        else:
                            break
                    else:
                        if(self.bfs[right_child] > self.bfs[parent]):
                            swap = self.bfs[parent]
                            self.bfs[parent] = self.bfs[right_child]
                            self.bfs[right_child] = swap
                            parent = right_child
                        else:
                            break
                #print("After one iteration bfs = {0} i = {1}".format(self.bfs, i))
        print("After Heapifying ", self.bfs)

obj = Heap()
'''
obj.insert(13)
obj.insert(11)
obj.insert(19)
obj.insert(30)
obj.insert(25)
obj.insert(39)
obj.insert(40)
obj.insert(12)
'''
obj.insert(10)
obj.insert(20)
obj.insert(15)
obj.insert(12)
obj.insert(40)
obj.insert(25)
obj.insert(18)

obj.bfs_tree_to_array()
obj.heapify()
