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
    def ThemNodePhiaTruoc(self):
        if self.head == None:
            return None
        
        #Tao node dau tien la 1
        p = Node(1)
        p.next = self.head
        self.head = p

        cur = p.next
        i = 2
        while cur.next: # cur != None
            p = Node(i)
            p.next = cur.next # Tao lien ket ben phai
            cur.next = p #Tao lien ket ben trai
            cur = p.next #Cap nhat lai node cur
            i+=1
    def printList(self):
        cur = self.head
        while cur:
            print(cur.data,end=" ")
            cur = cur.next
lst = LinkedList()
while True:
    n = int(input())
    if n == 0:
        break
    lst.insertTail(n)
lst.ThemNodePhiaTruoc()
lst.printList()