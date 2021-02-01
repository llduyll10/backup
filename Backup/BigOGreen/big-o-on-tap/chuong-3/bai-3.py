min = 11
max = -1
while True:
    a = int(input())
    if(a>max):
        max = a
    if(a<min and a != -1):
        min = a
    if(a==-1):
        break
print(max,min)
