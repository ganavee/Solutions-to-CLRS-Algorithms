class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None
        self.max_heap = []

    def insert(self, data):
        #Inserting the element in the array
        #insert at the end for the first time
        self.max_heap.append(data)
    
        #find the right position of the element
        index = length = len(self.max_heap) - 1
        if(length == 0):
            print("Max Heap Array ", self.max_heap)
            return
        while(index > 0):
            if(index%2 == 0):
                parent_index = index//2 - 1
            else:
                parent_index = index//2
            if(parent_index < length and parent_index >= 0):
                if(self.max_heap[parent_index] < data):
                    swap = data
                    self.max_heap[index] = self.max_heap[parent_index]
                    self.max_heap[parent_index] = swap
                    index = parent_index
                else:
                    break
        print("Max Heap Array ", self.max_heap)

    def convert_array_to_tree(self):
        self.head = Node(self.max_heap[0])
        curr = self.head
        queue = [curr]
        size = len(self.max_heap)
        if(size%2 == 0):
            length = size//2 -1
        else:
            length = size//2
        for i in range(length+1):
            curr = queue.pop(0)
            curr.left = Node(self.max_heap[2*i + 1])
            if(2*i + 2 < size):
                curr.right = Node(self.max_heap[2*i + 2])
            queue.append(curr.left)
            queue.append(curr.right)
        print("Done converting Max Heap Array to Tree")
            
                

    def delete(self):
        pass

    def display_dfs(self):
        curr = self.head
        queue = [curr]
        bfs = []
        curr = queue.pop()
        while(curr):
            bfs.append(curr.data)
            queue.append(curr.left)
            queue.append(curr.right)
            curr = queue.pop(0)
        print("BFS traversal ", bfs)


obj = Tree()
obj.insert(140)
obj.insert(150)
obj.insert(56)
obj.insert(130)
obj.insert(145)
obj.insert(65)
obj.insert(40)
obj.insert(160)
obj.convert_array_to_tree()
obj.display_dfs()
