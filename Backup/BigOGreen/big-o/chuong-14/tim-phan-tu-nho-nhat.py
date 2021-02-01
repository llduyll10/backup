import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def addToNode(self,x):
        if(x<self.data):
            if(self.left): #Neu co selft.left => Gọi đệ qui: left.addToNode(x)
                self.left.addToNode(x)
            else: #Nếu left là NULL / null / None, => Tạo node p => self.left = p
                self.left = Node(x)
        elif(x>self.data):
            if(self.right):#Neu co selft.right => Gọi đệ qui: right.addToNode(x)
                self.right.addToNode(x)
            else:  #Nếu right là NULL / null / None, => Tạo node p => self.right = p
                self.right = Node(x)
        else: #Khong roi vao 2 truong hop tren => Khong lam gi ca
            return
    def minNode(self): #Nếu nút hiện tại có con trái thì trả về min bên trái, nếu không thì trả về giá trị.
        if(self.left):
            return self.left.minNode()
        else:
            return self.data

class BinarySearchTree():
    def __init__(self):
        self.root = None
    def addToBST(self,data=0):
        if(self.root is None):
            self.root = Node(data)
        else:#Neu ma node root != None => goi hom addToNode de tao ra node moi
            self.root.addToNode(data)
    def min(self):
        return self.root.minNode()

T = BinarySearchTree()
n = int(input())
a = map(int,input().split())
for x in a:
    T.addToBST(x)

print(T.min())