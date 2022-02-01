'''To implement a stack using two queues'''

#Push = O(1) pop = O(n)
class Stack():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.current_queue = 1

    def push_item(self, item):
        if(self.current_queue == 1):
            self.queue1.append(item)
        else:
            self.queue2.append(item)

    def pop_item(self): 
        if(self.current_queue == 1):
            length = len(self.queue1)
            self.current_stack = 2
            if(length == 0):
                print("Stack Empty")
            else:
                for i in range(length-1):
                    self.push_item(self.queue1.pop(0))
                print("The popped element is ", self.queue1.pop(0))
        else:
            length = len(self.queue2)
            self.current_stack = 1
            if(length == 0):
                print("Stack Empty")
            else:
                for i in range(length-1):
                    self.push_item(self.queue2.pop(0))
                print("The popped element is ", self.queue2.pop(0))


obj = Stack()
obj.push_item('a')
obj.push_item('b')
obj.push_item('c')
obj.pop_item()
obj.pop_item()
obj.push_item('d')
obj.push_item('e')
obj.pop_item()
obj.push_item('f')
obj.pop_item()
obj.pop_item()
obj.pop_item()
obj.pop_item()
obj.pop_item()
obj.push_item('a')
obj.pop_item()
