'''Basic Queue Operations'''


class Queue_imp():

    def __init__(self):
        self.size = 3
        self.head = -1
        self.tail = -1
        self.queue = [None] * self.size

    def enqueue(self, item):
        if(not(self.if_full())):
            self.queue[self.tail] = item
            if(self.tail == 0):
                self.head = 0
            self.display()

    def dequeue(self):
        if(not(self.is_empty())):
            print("Dequeued Element is ", self.queue[self.head])
            self.head += 1
            if(self.head > self.tail):
                self.head = self.tail = -1
            self.display()
        pass

    def is_empty(self):
        if(self.head == -1):
            print("Queue is Empty")
            return True
        return False

    def if_full(self):
        self.tail += 1
        if(self.tail == self.size):
            print("Queue is Full")
            self.tail -= 1
            return True
        return False

    def display(self):
        if(not(self.is_empty())):
            print("Queue Elements are ", end = "")
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end = " ")
            print()

obj = Queue_imp()
obj.dequeue()
obj.enqueue(10)
obj.dequeue()
obj.enqueue(10)
obj.enqueue(6)
obj.dequeue()
obj.dequeue()
obj.enqueue(17)
obj.enqueue(37)
obj.enqueue(16)
obj.enqueue(67)
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
