n,X = map(int,input().split())
adj_matrix = []

for i in range(n):
    new_row = list(map(int,input().split()))
    adj_matrix.append(new_row)

#Vi X la 1 dinh trong do thi => Neu a[X][j] == 1 => X co lien ket voi 1 dinh khac 
count = 0
for j in range(n):
    if adj_matrix[X][j] == 1:
        count += 1
print(count)


