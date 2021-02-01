class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def addToNode(self,x):
        if(x<self.data):
            if(self.left): #Neu ma co left => goi de qui lai ham addToNode
                self.left.addToNode(x) 
            else:
                self.left = Node(x)
        elif(x>self.data):
            if(self.right):
                self.right.addToNode(x)
            else: #Neu ma self.right == None => tao node p => self.right = node p
                self.right = Node(x)
        else:
            return
    # Inorder traversal: Left – Node – Right.
    # Dùng để duyệt câu theo thứ tự tăng dần    
    def printInorder(self):
        #Vi yeu cau la tang dan => thu tu la left => node =>right
        if(self.left):
            self.left.printInorder()
        print(self.data,end=" ")
        if(self.right):
            self.right.printInorder()

class BST:
    def __init__(self):
        self.root = None
    def addToBST(self,data=0):
        if(self.root is None): #Neu self.root = None => self.root = NODE(P)
            self.root = Node(data)
        else: #Neu ma node root != None => goi hom addToNode de tao ra node moi
            self.root.addToNode(data)
    def printInorder(self): 
    #Hàm in các nút trong cây theo thứ tự inorder. Hàm này chỉ cần gọi lại hàm in các nút theo thứ tự inorder.
        self.root.printInorder()

T = BST()
n = int(input())
a = map(int,input().split())

for x in a:
    T.addToBST(x)

T.printInorder()