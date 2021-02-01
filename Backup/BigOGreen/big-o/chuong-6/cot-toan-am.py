def isAllNegatives(a, m, n, col):  
    flag = True  
    for i in range(m):  
        if(a[i][col] >= 0):  
            flag = False  
    return flag  
a = []  
m, n = map(int, input().split(' '))  
for i in range(m):  
    tmp = list(map(int, input().split()))  
    a.append(tmp)  
  
for j in range(n):  
    if isAllNegatives(a, m, n, j):  
        print(j, end = ' ')