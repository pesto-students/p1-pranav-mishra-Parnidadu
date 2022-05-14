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

    def rotate(self, k):
        if k == 0:
            return
         
        # Let us understand the below code for example k = 4
        # and list = 10->20->30->40->50->60
        current = self.head
         
        # current will either point to kth or NULL after
        # this loop
        # current will point to node 40 in the above example
        count = 1
        while(count <k and current is not None):
            current = current.next
            count += 1
     
        # If current is None, k is greater than or equal
        # to count of nodes in linked list. Don't change
        # the list in this case
        if current is None:
            return
 
        # current points to kth node. Store it in a variable
        # kth node points to node 40 in the above example
        kthNode = current
     
        # current will point to last node after this loop
        # current will point to node 60 in above example
        while(current.next is not None):
            current = current.next
        current.next = self.head
        self.head = kthNode.next
        kthNode.next = None

linkList = LL()

linkList.insert_end(1)
linkList.insert_end(2)
linkList.insert_end(3)
linkList.insert_end('July')
linkList.print_LL()
print("Linked list after rotate")
linkList.rotate(2)
linkList.print_LL()
