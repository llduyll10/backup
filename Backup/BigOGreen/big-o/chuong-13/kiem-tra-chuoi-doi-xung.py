# a là mảng(chuỗi) truyền vào.
# l là chỉ số của phần tử bên trái nhất của mảng hiện tại.
# r là chỉ số của phần tử bên phải nhất của mảng hiện tại
def check(a,l,r):
    if(l == r):
        return True #Nếu l == r (có nghĩa là mảng đang xét chỉ có một phần tử) -> Trả về TRUE.
    if(l == r -1 and a[l] == a[r]):
#Nếu l == r - 1 (mảng chỉ còn lại 2 phần tử), 
# ta kiểm tra xem a[l] có bằng a[r] không, nếu a[l] == a[r] -> Trả về TRUE, 
# ngược lại trả về FALSEFALSE.
        return True
    if(a[l] == a[r]):
#Nếu mảng nhiều hơn 2 phần tử và a[l] == a[r]
# ta gọi hàm đệ quy check(a, l+1, r-1)
        return check(a,l+1,r-1)
    return False


n = int(input())
str = input()
if(check(str,0,n-1)):
    print("YES")
else:
    print("NO")