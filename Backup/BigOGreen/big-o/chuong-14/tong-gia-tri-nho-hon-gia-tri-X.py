import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def addToNode(self,x):
        if(x<self.data):
            if(self.left):
                self.left.addToNode(x)
            else:
                self.left = Node(x)
        elif(x>self.data):
            if(self.right):
                self.right.addToNode(x)
            else:
                self.right = Node(x)
        else:
            return
    def TongGiaTriNhoHon(self,X):
        tong = 0
        if(self.data < X):
            tong += self.data
        if(self.left):
            tong += self.left.TongGiaTriNhoHon(X)
        if(self.right):
            tong += self.right.TongGiaTriNhoHon(X)
        return tong

class BST:
    def __init__(self):
        self.root = None
    def addToBST(self,data):
        if(self.root):
            self.root.addToNode(data)
        else:
            self.root = Node(data)
    def TongNhoHonX(self,X):
        return self.root.TongGiaTriNhoHon(X)

T = BST()
n,X = map(int,input().split(' '))
a = map(int,input().split(' '))

for x in a:
    T.addToBST(x)

print(T.TongNhoHonX(X))