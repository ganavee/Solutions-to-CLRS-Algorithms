class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None
        self.max_heap = []
        self.heap_sort = []
        
    #Inserting using the array
    def insert(self, data):
        #Inserting the element in the array
        #insert at the end for the first time
        self.max_heap.append(data)
    
        #find the right position of the element
        index = length = len(self.max_heap) - 1
        if(length == 0):
            print("After inserting {0} to Max Heap Array {1}".format(data, self.max_heap))
            print()
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
        print("After inserting {0} to Max Heap Array {1}".format(data, self.max_heap))
        print()

    def convert_array_to_tree(self):
        self.head = Node(self.max_heap[0])
        curr = self.head
        queue = [curr]
        size = len(self.max_heap)
        if(size%2 == 0):
            length = size//2 - 1
        else:
            length = size//2 - 1
        for i in range(length+1):
            curr = queue.pop(0)
            curr.left = Node(self.max_heap[2*i + 1])
            if(2*i + 2 < size):
                curr.right = Node(self.max_heap[2*i + 2])
            queue.append(curr.left)
            queue.append(curr.right)
        #print("Done converting Max Heap Array to Tree")
            
                
    #Deleting using the array
    def delete(self):
        #Replace root node with last node
        length = len(self.max_heap) - 1
        self.heap_sort.append(self.max_heap[0])
        #print("Heap_sort ", self.heap_sort)
        self.max_heap[0] = self.max_heap[length]
        
        #Remove the last node
        self.max_heap.pop()
        length -= 1
        #print("After replacing deleting {0} length {1}".format(self.max_heap, length))
        #Find the correct position for new root node
        parent = 0
        while(True): 
            left_child = 2*parent + 1
            right_child = 2*parent + 2
            if(left_child > length):
                break
            elif(left_child == length):
                if(self.max_heap[left_child] > self.max_heap[parent]):
                    swap = self.max_heap[parent]
                    self.max_heap[parent] = self.max_heap[left_child]
                    self.max_heap[left_child] = swap
                    parent = left_child
                else:
                    break
            else:
                if(self.max_heap[left_child] > self.max_heap[right_child]):
                    if(self.max_heap[left_child] > self.max_heap[parent]):
                        swap = self.max_heap[parent]
                        self.max_heap[parent] = self.max_heap[left_child]
                        self.max_heap[left_child] = swap
                        parent = left_child
                    else:
                        break
                else:
                    if(self.max_heap[right_child] > self.max_heap[parent]):
                        swap = self.max_heap[parent]
                        self.max_heap[parent] = self.max_heap[right_child]
                        self.max_heap[right_child] = swap
                        parent = right_child
                    else:
                        break
        print("After deleting  root element from Max heap array = ", self.max_heap)
        print()
        return

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
        print("BFS traversal of the Tree", bfs)
        print()

    def heap_sorting(self):
        while(len(self.max_heap)):
            self.delete()
        print("Sorting elements using heap sort ", self.heap_sort)


obj = Tree()
obj.insert(140)
obj.insert(150)
obj.insert(40)
obj.insert(130)
obj.insert(145)
obj.insert(65)
obj.insert(56)
obj.insert(160)
obj.insert(72)
obj.insert(23)
obj.insert(46)
obj.insert(70)
#obj.insert(45)
obj.convert_array_to_tree()
obj.display_dfs()
#obj.delete()
#obj.convert_array_to_tree()
#obj.display_dfs()
obj.heap_sorting()

