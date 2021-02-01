import sys
sys.setrecursionlimit(100000)

class SinhVien:
    def __init__(self,id,ten,diem):
        self.id = id
        self.ten = ten
        self.diem = diem

class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def addToNode(self,x):
        if(x.diem < self.data.diem):
            if(self.left):
                self.left.addToNode(x)
            else:
                self.left = Node(x)
        elif(x.diem > self.data.diem):
            if(self.right):
                self.right.addToNode(x)
            else:
                self.right = Node(x)
        else:
            return
    def SV_Best(self):
        #Vi la cao diem => kiem tra self.right => Neu co self.right thi tiep tuc de quy lai hamSV_Best
        if(self.right): 
            return self.right.SV_Best()
        return self.data #Con neu khong co thi tra ra gia tri cua node dang xet
class BST:
    def __init__(self):
        self.root = None
    def addToBST(self,x):
        if(self.root):
            self.root.addToNode(x)
        else:
            self.root = Node(x)
    def TimSVBest(self):
        return self.root.SV_Best()

T = BST()
n = int(input())

for i in range(n):
    id,ten,diem = input().split()
    diem = float(diem)
    T.addToBST(SinhVien(id,ten,diem))

ans = T.TimSVBest()
print(ans.id,ans.ten,ans.diem)