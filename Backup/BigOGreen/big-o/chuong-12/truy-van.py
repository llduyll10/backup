#Co 2 ham trong linked list => delete head va insertTail
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
            self.tail = p  #Cap nhat lai node tail la node p
    def deleteHead(self):
        if self.head == None:
            return
        self.head = self.head.next
    def printList(self):
        cur = self.head
        while cur:
            print(cur.data,end=" ")
            cur = cur.next #Cap nhat cur la node tiep theo
lst = LinkedList()
n = int(input())
for _ in range(n):
    s = input()
    if len(s) == 1:
        lst.deleteHead()
    else:
        x = int(s[2:])
        lst.insertTail(x)

lst.printList()
# Đối với ngôn ngữ PYTHON, do có dòng sẽ có 2 số, có dòng có một số, ta sẽ kiểm tra truy vấn đó là truy vấn nào bằng cách kiểm tra độ dài của một hàng ta đọc vào từ truy vấn:
# Lặp n lần (đề đoc truy vấn):
# S = input()S=input() (chuỗi SS là chuỗi chưa cả truy vấn).
# Nếu độ dài S = 1S=1:
# Thực hiện truy vấn 0.
# Ngược lại:
# Lấy xx ra bằng câu lệnh: x = int(S[2:])x=int(S[2:]) (Do S = “1 x”, ta sẽ bỏ phần “1 “ để lấy xx).
# Thực hiện truy vấn 2 với xx.

