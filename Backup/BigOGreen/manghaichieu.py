m,n = map(int,input().split( ))
a = []
for i in range(m):
    temp = list(map(int, input().split()))
    a.append(temp)

def tongDong(a):
    S=0
    for i in range(0,len(a),1):
        S=0
        for j in range(0,len(a[0]),1):
            S+=a[i][j]
        print("{0}: {1}".format(i,S))
# tongDong(a)

# Cot toan am
#Gia su toan bo toan am
def cotToanAm(a):
    for j in range(0,len(a[0]),1):
        flag = True
        for i in range(0,len(a),1):
            if(a[i][j]>=0):
                flag= False
        if(flag):
            print(j,end=" ")
# cotToanAm(a)
def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,n-1,2) :
        if n%i==0:
            return False
    return True

def demSNTBien(a):
    # Dem tren bien tren va bien duoi
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    count = 0
    # Duyet tren cot n

    for i in range(0,len(a[0]),1):
        if isPrime(a[0][i]):
            count += 1
        
    for i in range(0,len(a[0]),1):
        if isPrime(a[m-1][i]):
            count += 1
    for i in range(1,len())
    print(count)
demSNTBien(a)

            

# S=0
# count=0
# for i in range(m):
#     for j in range(n):
#        if(count<m):
#            print(a[count][j])
#            S+=a[count][j]
#            print(S)
#            count+=1
           
            
