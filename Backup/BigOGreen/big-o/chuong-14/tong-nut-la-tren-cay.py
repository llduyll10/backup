import sys
sys.setrecursionlimit(100000)
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def addToNode(self, x):
        if(x < self.data):
            if(self.left):
                self.left.addToNode(x)
            else:
                self.left = Node(x)
        elif(x > self.data):
            if(self.right):
                self.right.addToNode(x)
            else:
                self.right = Node(x)
        else:
            return

    def isLeaf(self):  # Node ma không có node left và node right
        return self.left is None and self.right is None

    def sumLeafNode(self):
        # Hàm trả về tổng các nút lá trong cây.
        # Bạn khởi tạo sum = 0.
        # Nếu có con trái:
        # sum sẽ cộng thêm cho tổng các nút lá trái
        # Nếu có con phải:
        # sum sẽ cộng thêm tổng các nút lá phải
        # Nếu nút hiện tại là nút lá:
        # thì trả về giá trị data
        # Còn không thì trả về sum.
        sum = 0
        if(self.left):
            sum += self.left.sumLeafNode()
        if(self.right):
            sum += self.right.sumLeafNode()
        if self.isLeaf():
            return self.data  # neu no la node la => return ve gia tri
        return sum


class BST:
    def __init__(self):
        self.root = None

    def addToBST(self, data):
        if(self.root is None):
            self.root = Node(data)
        else:
            self.root.addToNode(data)
    def sumLeafBST(self):
        return self.root.sumLeafNode()

T = BST()
n = int(input())
a = map(int, input().split())

for x in a:
    T.addToBST(x)
x = T.sumLeafBST()
print(x)