def reverse(n):
    ans = 0
    while n != 0:
        ans = ans * 10 + n % 10
        n = n // 10
    return ans
def isMatch(n):
    return n == reverse(n)

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None #Khoi tao node dau tien none
        self.tail = None #Khoi tao node cuoi cung la none
    def insertTail(self,data):
        p = Node(data)

        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p #Tao lien ket cho node p vs node tail
            self.tail = p #Cap nhat node tail la node p
    def InViTriCuaSDXTrongList(self):
        cur = self.head
        i = 0
        while cur:
            if isMatch(cur.data):
                print(i,end=" ") 
            i += 1
            cur = cur.next

lst = LinkedList()
while True:
    n = int(input())
    if n == -1:
        break
    lst.insertTail(n)

lst.InViTriCuaSDXTrongList()