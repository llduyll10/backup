

# n = int(input())
# arr = list(map(int, input().split()))

# flag = False
# Flag = False
# for i in range(0, len(arr), 1):
    
#     if i < len(arr):
#         if(arr[i] == 0 and arr[i+1] == 0):
#             flag = True
#             if flag:
#                 if(arr[i] == 0 and arr[i+2] == 0):
#                     Flag = True
#         else:
#             flag = False
# if Flag:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# arr = list(map(int,input().split()))

# boy = 0
# girl = 0
# for i in range(0,len(arr),1):
#     if(arr[i]==0):
#         boy+=1
#     if(arr[i]==1):
#         girl+=1
# if(boy==girl):
#     print('YES')
# else:
#     print('NO')


# min= arr[0]
# tong = 0
# for i in range(1,len(arr),1):
#     if(arr[i]<min):
#         min=arr[i]
# for i in range(0,len(arr),1):
#     if(arr[i]>=min):
#         tong += (arr[i]-min)
# print(tong)

# def isprime(n):
#     if n < 2:
#         return False
#     # 2 is the only even prime number
#     if n == 2:
#         return True
#     # all other even numbers are not primes
#     if not n & 1:
#         return False
#     # range starts with 3 and only needs to go up the squareroot of n
#     # for all odd numbers
#     for x in range(3, int(n**0.5)+1, 2):
#         if n % x == 0:
#             return False
#     return True

# n = int(input())
# arr = list(map(int,input().split()))
# count = 0
# for i in range(0,len(arr),1):
#     if(isprime(arr[i])):
#         count+=1

# print(count)
# n = int(input())
# arr = list(map(int,input().split()))
# flag = True
# for i in range(0,len(arr),1):

#     if(arr[i]==0):
#         flag=False
# if flag:
#     print('YES')
# else:
#     print('NO')

# for i in range(0,len(arr),1):
#     if(arr[i]%2==0):
#         print(arr[i])

# n = int(input())
# arr = list(map(int,input().split()))
# max=arr[0]
# for i in range(1,n,1):
#     if(arr[i]>max):
#         max=arr[i]

# print(max)


# n = int(input())
# arr = list(map(int,input().split()))

# Tong= 0
# for i in range(0,len(arr),1):
#     Tong += arr[i]

# print(Tong)


# Code forces 787A
# a,b = map(int,input().split())
# c,d = map(int,input().split())

# def GCD(a,b):
#     tmp=0
#     while(b != 0):
#         tmp = a%b
#         a=b
#         b=tmp
#     return a

# X=GCD(a,c)
# if((d-b)% X !=0):
#     print(-1)
# else:
#     y=0
#     while True:
#         x=(d+c*y-b)//a
#         if(x>=0 and (d+c*y-b)%a==0):
#             print(b+a*x)
#             break
#         y+=1


# temp=True
# s1 = int(input())
# while True:
#     a = int(input())
#     if(a<s1):
#         temp=False
#     if(a==0):
#         break
# a = int(input())
# count = 0
# i=1

# while i<=a:
#     s=int(input())
#     if(s%2!=0):
#         count+=1
#     i+=1
# if(count>0):
#     print('YES')
# else:
#     print('NO')
# print(count)

# while i <= a:
#     b = int(input())
#     if(b%2==0):
#         flag = True
#     else:
#         flag = False
#     i+=1


# flag = True
# hprev = 0
# while True:
#     a = int(input())
#     if(a<hprev):
#         flag= False
#         hprev = a
#     if(a == 0):
#         break
# if flag:
#     print('YES')
# else:
#     print('NO')

# max=-1
# min=11
# while True:
#     a=int(input())
#     if(a>max):
#         max=a
#     if(a<min and a != -1):
#         min=a
#     if(a==-1):
#         break
# print(max, min)


# count=0
# while True:
#     a = int(input())
#     if(a == 5):
#         count +=1
#     if(a==0):
#         break
# print(count)

# a = int(input())
# S = 0
# for i in range(0,a+1,1):
#     S+=i
# print(S)

# a,b = map(int,input().split())
# c=a*b
# print(c//2)

# a = int(input())

# if(a%5==0):
#     r1=a/5
#     print(int(r1))
# else:
#     r1 = a //5 +1
#     print(int(r1))


# a,b,c = map(int,input().split())
# if(a%c==0):
#     r1=a//c
# else:
#     r1=a//c +1
# if(b%c==0):
#     r2= b//c
# else:
#     r2= b//c +1
# print(r1*r2)


#  a=int(input())
# if(a<4):
#     print('No')
# elif(a%2==0 and a>=4):
#     print('Yes')
# else:
#     print('No')

# a=int(input())

# if( a%400 == 0):
#     print('YES')
# elif(a%4==0 and a%100==0):
#     print('NO')
# elif(a%4==0):
#     print('YES')
# else:
#     print('NO')

# a = int(input())

# if (a == 1 or a == 2 or a == 3):
#     print(1)
# elif (a == 4 or a == 5 or a == 6):
#     print(2)
# elif (a == 7 or a == 8 or a== 9):
#     print(3)
# else:
#     print(4)

# a,b = map(int, input().split())

# if a>0 and b>0:
#     print('YES')
# elif a<0 and b<0:
#     print('YES')
# else:
#    print('NO')
