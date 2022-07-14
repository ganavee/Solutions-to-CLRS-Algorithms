import sys
class ListNode:
    def __init__(self, value, nxt = None):
        self.val = value
        self.next = nxt


class Singly_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, val, nxt = None):
        if(self.head == None):
            node = ListNode(val, nxt)
            self.head = node
            self.tail = self.head
            #self.display(self.head)
            return (self.head, node)
        node = ListNode(val, nxt)
        self.tail.next = node
        self.tail = self.tail.next
        #self.display(self.head)
        return (self.head, node)

    def length_of_cycle(self):
       
        slow = fast = self.head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                slow = slow.next
                count = 1
                while(slow != fast):
                    count += 1
                    slow = slow.next
                return print("Length of cycle in Linked List ", count)
                
        return print("Length of Cycle = 0")
        
        pass
        
    def display(self, head):
        temp = head
        while(temp):
            print("{0}-->".format(temp.val), end="")
            temp = temp.next
        print("END")
        
        
obj = Singly_list()
head1, node = obj.insert(2)
head1, node = obj.insert(3)
head1, node = obj.insert(15)
temp = node
head1, node = obj.insert(23)
head1, node = obj.insert(29)
head1, node = obj.insert(87)
#head1, node = obj.insert(5, temp)
print("List1")
obj.length_of_cycle()
#obj.display(head1)

