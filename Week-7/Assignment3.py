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

    def detectLoop(self):
        #returning True or False if there exist loop.
        s = set()
        temp = self.head
        while (temp):
            # If we have already has
            # this node in hashmap it
            # means their is a cycle
            if (temp in s):
                return True
 
            s.add(temp)
 
            temp = temp.next
 
        return False

linkList = LL()

linkList.insert_end(1)
linkList.insert_end(2)
linkList.insert_end(3)
linkList.insert_end('July')

# Creating loop for detection

linkList.head.next.next.next.next = linkList.head
if linkList.detectLoop:
    print("Loop exist in the linked list")
else:
    print("Loop doesn't exist in this linked list")