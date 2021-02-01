# Với gợi ý từ đề bài, chu trình Euler trong đồ thị vô hướng khi và chỉ khi mọi đỉnh đều có bậc chẵn. 
# Vậy ta sẽ cần kiểm tra từng đỉnh xem có thỏa điều kiện là số bậc chẵn. 
# Được biết bậc của 1 đỉnh trong đồ thị vô hướng được tính bằng tổng số cạnh nối tới đỉnh đó.

n = int(input())
adj_matrix =[]

for i in range(n):
    new_row = list(map(int,input().split()))
    adj_matrix.append(new_row)


flag = True
for i in range(n):
    count = 0
    for j in range(n):
        count += adj_matrix[i][j]
    if count % 2 != 0:
        flag = False

if(flag):
    print('YES')
else:
    print('NO')