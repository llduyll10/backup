a = 5
b = 6
c = 7
if b>a:
    print("b>a")
elif a==b:
    print("a==b")
else:
    print("b<a")

#Or and And
if a<b and b<c:
    print("a<c")
if a<b or b<c:
    print("or a<c")

#while loop

i=0
while i <6:
    print(i)
    if i == 3:
        break
    i+=1

#for loop
fruits = ["mango","banana","melon"]
for x in fruits:
    print(x)

#for loop through a String
for x in "DuyNND":
    print(x)
