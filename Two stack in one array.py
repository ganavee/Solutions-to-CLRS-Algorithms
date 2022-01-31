'''Implement  two stacks in one array A[1..n] in such a way that
neither stack overflows unless the total number of elements in both
stacks together is n. The PUSH and POP operations should run in O(1) time.'''


class Stack():
    
    def __init__(self):
        #enter the size of the array
        self.n = int(input("Enter the size of array "))
        self.top_left = -1
        self.top_right = self.n
        self.stack = [None] * self.n
        print(self.stack)

    def push(self, stack_num, item):
        if(stack_num ==  1):
            if(not(self.stack_overflow(stack_num))):
                self.stack[self.top_left] = item
                self.display(self.top_left, stack_num)
            else:
                self.top_left -= 1
        else:
            if(not(self.stack_overflow(stack_num))):
                self.stack[self.top_right] = item
                self.display(self.top_right, stack_num)
            else:
                self.top_right += 1
        

    def pop(self, stack_num):
        if(stack_num == 1):
            if(not(self.stack_empty(stack_num))):
                self.stack[self.top_left] = None
                self.top_left -= 1
                self.display(self.top_left, stack_num)
                
                
        else:
            if(not(self.stack_empty(stack_num))):
                self.stack[self.top_right] = None
                self.top_right += 1
                self.display(self.top_right, stack_num)
                

    def stack_overflow(self, stack_num):
        if(stack_num ==  1):
            self.top_left += 1
        else:
            self.top_right -=  1
        if(self.top_left == self.top_right):
            print("Stack Full")
            return True
        return False

    def stack_empty(self, stack_num):
        if(stack_num == 1 and self.top_left == -1):
            print("Left stack empty")
            return True
        elif(stack_num == 2 and self.top_right == self.n):
            print("Right stack empty")
            return True
        return False
    
    def display(self, top, stack_num):
        if(stack_num == 1):
            print("Left Array ", end = " ")
            for i in range(0, top+1):
                print(self.stack[i], end = " ")
        else:
            print("Right Array ", end = " ")
            for i in range(self.n-1, top - 1, -1):
                print(self.stack[i], end = " ")
        print()
        print("Complete array ", self.stack)

obj = Stack()
obj.push(1, 10)
obj.push(2, 60)
obj.push(1, 45)
obj.push(2, 78)
obj.push(1, 97)
obj.push(2, 34)
obj.push(1, 0)
obj.pop(1)
obj.pop(1)
obj.pop(1)
obj.pop(1)
obj.pop(1)
obj.pop(1)
obj.pop(2)
obj.pop(2)
obj.pop(2)
obj.pop(2)
obj.pop(2)
obj.pop(2)
obj.push(1, 10)
obj.push(2, 60)
obj.push(1, 45)
obj.push(2, 78)
obj.push(1, 97)
obj.push(2, 34)
obj.push(1, 0)
