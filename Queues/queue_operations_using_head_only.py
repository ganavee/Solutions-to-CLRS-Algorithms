import sys

class Queue:
    def __init__(self):
        self.size = 3
        self.queue = [None] * self.size
        self.ptr = -1
        self.curr_size = 0
        
        pass

    def enqueue(self):
        if(self.curr_size == self.size):
            print("Queue full")
            return
        print("Enter the element")
        ele = int(sys.stdin.readline().strip())
        self.queue[self.curr_size] = ele
        print("{0} Added to the Queue".format(self.queue[self.curr_size]))
        self.curr_size += 1
        self.display()

    def display(self):
        for i in range(self.curr_size):
            print("{0}-->".format(self.queue[i]), end="")
        print("END")

    def dequeue(self):
        if(self.curr_size == 0):
            print("Queue is empty")
            return
        print("Removed item is ", self.queue[0])
        for i in range(1, self.curr_size):
            self.queue[i-1] = self.queue[i]
        self.curr_size -= 1
        self.display()
    

obj = Queue()
while(True):
    print("1. Enter 1 to insert\n2. Enter 2 to remove\n3. Enter 3 to Dispplay\n4. Enter 4 to quit")
    option = int(sys.stdin.readline().strip())
    if(option == 1):
        obj.enqueue()
    elif(option == 2):
        obj.dequeue()
    elif(option == 3):
        obj.display()
    else:
        print("PROGRAM TERMINATED")
        break
