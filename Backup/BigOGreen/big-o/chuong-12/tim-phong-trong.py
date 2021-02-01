class Room:
    def __init__(self,id=0,gia=0,status=0):
        self.id = id
        self.gia = gia
        self.status = status
class Node:
    def __init__(self,data = None):
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
            self.tail =p
    def TimPhongTrong(self):
        cur = self.head
        while cur:
            if cur.data.status == '0':
                print(cur.data.id, cur.data.gia)
            cur = cur.next
        
lst = LinkedList()
n = int(input())

for i in range(n):
    id,gia,status = input().split()
    lst.insertTail(Room(id,gia,status))

lst.TimPhongTrong()