#Trees in iterative


class Node:
    def __init__(self, val):
        self.ele = val
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if(self.root == None):
            self.root = Node(val)
            return
        temp = self.root
        queue = []
        queue.append(temp)
        index = 0
        while(index < len(queue)):
            curr = queue[index]
            if(curr.left == None):
                curr.left = Node(val)
                break
            queue.append(curr.left)
            if(curr.right == None):
                curr.right = Node(val)
                break
            queue.append(curr.right)
            index += 1
        

    def bfs(self):
        queue = []
        index = 0
        temp = self.root
        if(temp == None):
            print("Nothing to print")
            return
        queue.append(self.root)
        res = []
        res.append(self.root.ele)
        while(index < len(queue)):
            curr = queue[index]
            if(curr.left == None):
                break
            res.append(curr.left.ele)
            queue.append(curr.left)
            if(curr.right == None):
                break
            res.append(curr.right.ele)
            queue.append(curr.right)
            index += 1
        print("BFS: ", res)

    def preOrder(self):
        stack = []
        temp = self.root
        res = []
        if(temp == None):
            print("Nothing to print")
            return
        stack.append(self.root)
        while(len(stack) > 0):
            curr = stack.pop()
            #print("curr: ", curr)
            res.append(curr.ele)
            if(curr.right != None):
                stack.append(curr.right)
            if(curr.left != None):
                stack.append(curr.left)
            #print("stack: ", stack)
        print("Pre Order: ", res)
        

    def postOrder(self):
        stack = []
        temp = self.root
        res = []
        if(temp == None):
            print("Nothing to print")
            return
        stack.append(self.root)
        while(len(stack) > 0):
            curr = stack.pop()
            if(curr.left != None):
                stack.append(curr.left)
            if(curr.right != None):
                stack.append(curr.right)
            res.append(curr.ele)
        print("PostOrder: ", end = "")
        for i in range(len(res)-1, -1, -1):
            print(res[i], end = "")
            print(", ", end = "")
        

    def inOrder(self):
        stack = []
        temp = self.root
        res = []
        if(temp == None):
            print("Nothing to print")
            return
        curr = self.root
        while(True):
            if(curr != None):
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if(curr != None):
                    res.append(curr.ele)
                    curr = curr.right
            if(len(stack) == 0 and curr == None):
                break
        print("InOrder: ", res)
        

obj = Tree()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.insert(6)


obj.bfs()
obj.preOrder()
#obj.postOrder()
obj.inOrder()
