def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertTail(self,data): #Ky thuat insert vao cuoi phan tu
        p = Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    def demSNT(self):
        cur = self.head
        count = 0
        while cur: # Neu cur != None
            if isPrime(cur.data):
                count += 1
            cur = cur.next #Chuyrn qua node tiep theo de kiem tra
        print(count)

n = int(input())
dslk = LinkedList()

while n != -1:
    dslk.insertTail(n)
    n = int(input())

dslk.demSNT()

