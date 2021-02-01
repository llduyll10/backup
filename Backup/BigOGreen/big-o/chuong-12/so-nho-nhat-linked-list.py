class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertTail(self, data): #Ky thuat them x vao cuoi linked list
        p = Node(data) #Khoi tao node p
        if self.head == None: #Neu head == None => gan node head = node tail = node p
            self.head = self.tail = p
        else:
            self.tail.next = p #Nguoc lai => gan node tail = node p
            self.tail = p #sau do cho node p = node tail (node tail la node cuoi cung)
    
    def min(self):
        if self.head == None:
            return None
        res = self.head
        cur = self.head

        while cur:
            if cur.data < res.data:
                res = cur
            cur = cur.next
        
        return res

lst = LinkedList()
while True:
    n = int(input())
    if n==0:
        break
    lst.insertTail(n)

res = lst.min()
if res:
    print(res.data)
else:
    print(0)