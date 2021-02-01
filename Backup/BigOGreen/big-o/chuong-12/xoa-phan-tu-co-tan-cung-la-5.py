def checkLast5(n):
    return n % 10 == 5


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkdedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, data):
        p = Node(data)

        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p

    def removeLast5(self):
        #Remove thuc ra la tao lai lien ket
        #Tao ra 2 bien la cur,pre
        cur = self.head  # Ban dau node cur  la node head
        pre = None  # pre la node phia truoc node cur

        while cur:  # cur != None
            if checkLast5(cur.data):  # Neu node cur co data tan cung la 5
                if pre == None: #Neu node pre == NONE => node cur la node head
                    self.head = cur.next #Cap nhat lai node head
                    cur = cur.next
                elif self.tail == cur: #Neu node cur o cuoi danh sach va co tan cung la 5
                    pre.next = None #Cap nhat lai bien pre la node NONE
                    self.tail = pre #Cap nhat lai node  tail = node pre = node None
                else:
                    pre.next = cur.next #Tao lien ket
                    cur = cur.next #Cap nhat lai node cur la node tiep theo
            else:
                pre = cur
                cur = cur.next
    def printList(self):
        cur = self.head
        while cur:
            print(cur.data,end=" ")
            cur = cur.next

lst = LinkdedList()
n = int(input())
a = []

for i in range(n):
    x = int(input())
    a.append(x)

for x in a:
    lst.insertTail(x)

lst.removeLast5()
lst.printList()

