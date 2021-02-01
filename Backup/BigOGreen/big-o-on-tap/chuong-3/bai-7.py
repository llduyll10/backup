n = int(input())
#in hang dau tien
for i in range(1,n+1):
    print('*',end='')
print()

#in cac hang phia trong
for i in range(2,n):
    print('*',end='')
    for j in range(2,n):
        print(' ',end='')
    print('*')
#in hang cuoi cung
for i in range(1,n+1):
    print('*',end='')