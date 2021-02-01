class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None # Khoi tao node dau tien = None
        self.tail = None #Khoi tao node cuoi cung = None
    def insertTail(self,data): #Them 1 node vao sau list
        p = Node(data)

        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p #Tao lin ket
            self.tail = p #Cap nhat lai node cuoi cung la  node p
    def TimSoLonThuNhi(self):
        if self.head == None:
            return
        
        cur = self.head.next #Tao bien cur la node dung sau node head

        max1 = self.head.data #Gia su node dung sau node head la max value
        max2 = -1
        while cur:
            if cur.data > max1:
               max2 = max1
               max1 = cur.data
            elif cur.data > max2 and cur.data < max1:
                max2 = cur.data
            cur = cur.next
        return max2

lst = LinkedList()

while True:
    n = float(input())
    if n == -1:
        break
    lst.insertTail(n)

res = lst.TimSoLonThuNhi()
print(res)