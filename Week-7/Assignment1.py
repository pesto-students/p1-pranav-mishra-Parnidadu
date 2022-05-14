class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LL(Node):
    def __init__(self):
        self.head = None

    def insert_end(self,data):
        node = Node(data)
        if self.head ==None:
            self.head = node
            return
        
        last = self.head
        while(last.next):
            last = last.next
        last.next = node
    
    def print_LL(self):
        if self.head == None:
            return "Linked List is empty"
        # print(self.head.next)
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next
        print('-'*50)

    def reverse_LL(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


linkList = LL()

linkList.insert_end(1)
linkList.insert_end(2)
linkList.insert_end(3)
linkList.insert_end('July')
linkList.print_LL()
print("Linked list after reverse")
linkList.reverse_LL()

linkList.print_LL()



