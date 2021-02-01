class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def isNewDate(self, other):
        return self.year > other.year or (self.year == other.year and (self.month > other.month or (self.month == other.month and self.day > other.day)))

    def __str__(self):
        return str(self.day) + " " + str(self.month) + " " + str(self.year)

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
            self.tail.next = p #Tao lien ket
            self.tail = p #Cap nhat lai node tail la node p
    def getLastedDate(self):
        if self.head == None:
            return None
        cur = self.head
        res = self.head #Gia su ngay moi nhat la node head
        cur = cur.next #Cur la node dung sau node head

        while cur:
            if cur.data.isNewDate(res.data): #So sanh node sau va node truoc
                res = cur

            cur = cur.next
        return res

lst = LinkedList()
n = int(input())
for _ in range(n):
    d, m, y = list(map(int, input().split()))
    lst.insertTail(Date(d, m, y))

res = lst.getLastedDate()
if res:
    print(res.data)
else:
    print(0)

