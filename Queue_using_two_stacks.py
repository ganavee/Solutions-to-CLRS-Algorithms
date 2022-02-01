''''Show how to implement a queue using two stacks.'''

#pop costly method push O(1) and pop O(n)
class Queue1():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.current_stack = 1
    
    def enqueue(self, item):
        if(self.current_stack == 1):
            self.stack1.append(item)
        else:
            self.stack2.append(item)


    def dequeue(self):
        if(self.current_stack == 1):
            length = len(self.stack1)
            if(length == 0):
                print("Stack Empty")
            else:
                self.current_stack = 2
                for i in range(length, 1, -1):
                    self.enqueue(self.stack1.pop())
                print("Popped element ", self.stack1.pop())
                self.current_stack = 1
                length = len(self.stack2)
                for i in range(length, 0, -1):
                    self.enqueue(self.stack2.pop())
                    self.top2 -= 1
                    
#pop costly method push O(1) and pop O(n)
class Queue2():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.current_stack = 1
    def enqueue(self, item):
        if(self.current_stack == 1):
            self.stack1.append(item)
        else:
            self.stack2.append(item)

    def dequeue(self):
        if(len(self.stack2) == 0):
            length = len(self.stack1)
            if(length == 0):
                print("Stack empty")
            #Move all the elemens from Stack1 to Stack2
            else:
                self.current_stack = 2
                for i in range(length, 1, -1):
                    self.enqueue(self.stack1.pop())
                print("Popped Element is ", self.stack1.pop())
                self.current_stack = 1
                    
        else:
            print("Popped Element is ", self.stack2.pop())

obj = Queue2()
obj.enqueue(10)
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.enqueue(25)
obj.enqueue(36)
obj.enqueue(78)
obj.dequeue()
obj.enqueue(49)
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
