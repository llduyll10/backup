class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertTail(self,data):
        p = Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    def duoiTB(self):
        cur = self.head
        while cur:
            if cur.data < 5.0:
                print(cur.data)
            cur = cur.next

n = float(input())
dsDiem = LinkedList()

while n != -1:
    dsDiem.insertTail(n)
    n = float(input())

dsDiem.duoiTB()
        