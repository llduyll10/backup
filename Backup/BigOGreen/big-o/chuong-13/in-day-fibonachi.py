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
    def printList(self):
        cur = self.head

        while cur:
            print(cur.data,end=" ")
            cur = cur.next

x,y,n = map(int,input().split())
lst = LinkedList()
lst.insertTail(x)
lst.insertTail(y)

for i in range(n-2):
    cur = (x + y) % 1000007
    lst.insertTail(cur)
    x = y
    y = cur

lst.printList()