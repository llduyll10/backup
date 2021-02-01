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
    def isFullLeftRight(self):
        return self.left and self.right
    def countFullLeftRight(self):
        count = 0
        if(self.isFullLeftRight()):
            count += 1
        if(self.left):
            count += self.left.countFullLeftRight()
        if(self.right):
            count += self.right.countFullLeftRight()
        return count
class BST:
    def __init__(self):
        self.root = None
    def addToBST(self,data):
        if(self.root):
            self.root.addToNode(data)
        else:
            self.root = Node(data)
    def countFullLeftRightBST(self):
        return self.root.countFullLeftRight()

T = BST()
n = int(input())
a = map(int,input().split())

for x in a:
    T.addToBST(x)

print(T.countFullLeftRightBST())

