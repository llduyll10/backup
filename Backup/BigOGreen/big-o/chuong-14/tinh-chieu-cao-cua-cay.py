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
    def getHeightNode(self):
        # Bạn sẽ tính độ cao cây con bên phải (nếu có) và cây con bên trái (nếu có)
        heightLeft = 0
        heightRight = 0
        if(self.left):
            #Goi de quy ham getHeighNode de tinh chieu cao cay
            heightLeft = self.left.getHeightNode()
        if(self.right):
            heightRight = self.right.getHeightNode()
        return 1 + max(heightLeft,heightRight)


class BST:
    def __init__(self):
        self.root = None
    def addToBST(self,data):
        if(self.root is None):
            self.root = Node(data)
        else:
            self.root.addToNode(data)
    def getHeighBST(self):
         # Hàm trả về độ cao của cây. Hàm này chỉ cần gọi lại hàm trả về độ cao của cây có gốc self.
        return self.root.getHeightNode()

T = BST()
n = int(input())
a = map(int,input().split())

for x in a:
    T.addToBST(x)

print(T.getHeighBST())