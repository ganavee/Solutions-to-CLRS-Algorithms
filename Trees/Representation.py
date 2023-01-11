#Representing trees

class Node:
    def __init__(self, val):
        self.ele = val
        self.right = None
        self.left = None


class Insertion:
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

    def bfsRec(self, index, queue, res):
        if(index == len(queue)):
            return res
        curr = queue[index]
        if(curr.left != None):
            queue.append(curr.left)
            res.append(curr.left.ele)
        if(curr.right != None):
            queue.append(curr.right)
            res.append(curr.right.ele)
        return self.bfsRec(index+1, queue, res)

    def bfs(self):
        queue = []
        if(self.root == None):
            return queue
        queue.append(self.root)
        res = []
        res.append(self.root.ele)
        return self.bfsRec(0, queue, res)
        

    def preOrderRec(self, curr, res):
        if(curr == None):
            return res
        res.append(curr.ele)
        res = self.preOrderRec(curr.left, res)
        res = self.preOrderRec(curr.right, res)
        return res

    def preOrder(self):
        temp = self.root
        res = []
        return self.preOrderRec(temp, res)


    def postOrderRec(self, curr, res):
        if(curr == None):
            return res
        res = self.postOrderRec(curr.left, res)
        res = self.postOrderRec(curr.right, res)
        res.append(curr.ele)
        return res

    def postOrder(self):
        temp = self.root
        res = []
        return self.postOrderRec(temp, res)
    

    def inOrderRec(self, curr, res):
        if(curr == None):
            return res
        res = self.inOrderRec(curr.left, res)
        res.append(curr.ele)
        res = self.inOrderRec(curr.right, res)
        return res
        

    def inOrder(self):
        temp = self.root
        res = []
        return self.inOrderRec(temp, res)




obj = Insertion()
obj.insert(4)
obj.insert(5)
obj.insert(6)
obj.insert(7)
obj.insert(8)
obj.insert(9)
print("Inorder: ", obj.inOrder())
print("Postorder: ", obj.postOrder())
print("Preorder: ", obj.preOrder())
print("BFS: ", obj.bfs())
