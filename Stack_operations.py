'''Stack Operations'''


class Stack_imp():

    def __init__(self):
        self.size = 3
        self.stack = [None] * self.size
        self.top = -1
    
    def dummy(self):
        print(self.size)
        self.stack.append(10)
        self.top += 1
        print(self.stack, self.top)
        
    def push_item(self, item):
        if(not (self.stack_overflow())):
            self.stack[self.top] = item
        self.display()

    def pop_item(self):
        if(not (self.stack_empty())):
            print("Element popped = ", self.stack[self.top])
            self.top -= 1
            self.display()
                  

    def stack_overflow(self):
        self.top += 1
        if (self.top < self.size):
            return False
        self.top -= 1
        print("Stack Full")
        return True

    def stack_empty(self):
        if (self.top ==  -1):
            print("Stack Empty")
            return True
        return False

    def display(self):
        if(not(self.stack_empty())):
            print("Stack elements are ", end = "")
            for i in range(self.top+1):
                print(self.stack[i], end = " ")
            print()
            
obj = Stack_imp()
obj.pop_item()
obj.push_item(10)
obj.push_item(25)
obj.pop_item()
obj.pop_item()
obj.push_item(10)
obj.push_item(25)
obj.push_item(1)
obj.push_item(45)

