import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.right = right
        self.left = left
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
    def LietKeSoChan(self):
        if(self.left):
            self.left.LietKeSoChan()
        if(self.right):
            self.right.LietKeSoChan()
        if(self.data % 2 == 0):
            print(self.data,end=" ")

class BST:
    def __init__(self):
        self.root = None
    def addToBST(self,data):
        if(self.root):
            self.root.addToNode(data)
        else:
            self.root = Node(data)
    def LietKeChanBST(self):
        return self.root.LietKeSoChan()
T = BST()
n = int(input())
a = map(int,input().split())

for x in a:
    T.addToBST(x)
T.LietKeChanBST()
        
