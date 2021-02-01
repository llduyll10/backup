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
            self.tail = p
    def createNewList(self):
        if self.head == None:
            return None

        new_list = LinkedList()
        prev = None
        cur = self.head

        while cur != None:
            if cur == self.head:
                new_list.insertTail(cur.data)
            else:
                new_list.insertTail(prev.data + cur.data)

            prev = cur
            cur = cur.next
        return new_list
    def printList(self):
        cur = self.head
        while cur:
            print(cur.data,end=" ")
            cur = cur.next

lst = LinkedList()
n = int(input())
a = list(map(int,input().split()))

for x in a:
    lst.insertTail(x)

new_list = lst.createNewList()
new_list.printList()


