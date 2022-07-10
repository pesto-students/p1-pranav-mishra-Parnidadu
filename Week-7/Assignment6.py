import queue


class Queue:
    def __init__(self):
        self.arr = list()

    def add(self,data):
        self.arr.append(data)

    def pop(self):
        return self.arr.pop(0)

    def printQ(self):
        return self.arr

N =  int(input("Enter the number of operations"))
queu = Queue()
while(N):
    q = int(input("Enter 1 for adding and 2 for deleting"))
    if q==1:
        data = int(input("Enter the data you want to add"))
        queu.add(data)
    elif q==2:
        print(queu.pop())

    N-=1

print('Queue after the operation: ', queu.printQ())