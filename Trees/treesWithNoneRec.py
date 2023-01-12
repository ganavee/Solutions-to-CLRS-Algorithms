class Node:
    def __init__(self, val):
        self.ele = val
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def insertRec(self, val, index, queue):
        curr = queue[index]
        if(curr.left == None):
            curr.left = Node(val)
            return
        else:
            queue.append(curr.left)
        if(curr.right == None):
            curr.right = Node(val)
            return
        else:
            queue.append(curr.right)
        self.insertRec(val, index+1, queue)

    def insert(self, val):
        if(self.root == None):
            self.root = Node(val)
            return
        temp = self.root
        queue = []
        queue.append(self.root)
        index = 0
        self.insertRec(val, index, queue)

    def bfsRec(self, queue, index, res):
        if(index >= len(queue)):
            return res
        curr = queue[index]
        if(curr.ele != None):
            res.append(curr.ele)
        index += 1
        if(curr.left != None):
            queue.append(curr.left)
        if(curr.right != None):
            queue.append(curr.right)
        return self.bfsRec(queue, index, res)
            
        
    def bfs(self):
        if(self.root == None):
            print("No elements to print")
            return
        temp = self.root
        queue = []
        queue.append(self.root)
        index = 0
        res = []
        return self.bfsRec(queue, index, res)
        

obj = Tree()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.insert(None)
obj.insert(None)
obj.insert(None)
obj.insert(None)
obj.insert(6)
obj.insert(7)
obj.insert(None)
obj.insert(None)
obj.insert(None)
obj.insert(None)
print("BFS: ", obj.bfs())
