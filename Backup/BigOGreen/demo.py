print("Hello world!!");

#Dem so ky tu trong chuoi
a = "Hello Duy";
print(len(a));

#Xoa khoang trang dau va cuoi
b="  Hello, World     ";
print(b.strip());

#Chuyen thanh chu thuong
print(a.lower())

#Chuyen thanh chu hoa
print(b.upper());

#Replace ky tu
print(a.replace('H','111'))

#Cat chuoi ky tu
print(b.split(','));

#Check mot string co trong mot chuoi ko
print("World" in b)

tong=5;
hieu=4;
if tong>hieu:
    print('Tong lon hon hieu')
else:
    print('Tong nho hon hieu');

#Loop in List
thisList=['apple','banana','cherry']
for x in thisList:
    print(x)
#Check item exist in List
if "apple" in thisList:
    print('Yes apple')

#Check length
print('Length list',len(thisList))

#Addd item in List
thisList.append('melon')
print(thisList)

#Insert item in position you want
thisList.insert(1,"orange")
print(thisList)

#Remove item
thisList.remove("melon")
print(thisList)



#Delete all item in list
clearList = ["a","b","c"]
clearList.clear()
print(clearList)

#Coppy a List
coppyList = ["A","B","C"];
cloneCoppyList = coppyList.copy()
print(cloneCoppyList)

#Join two list
listA = [0,1,2]
listB = [3,4,5]
listC = listA + listB;
print(listC)


#Collection Tuple
thisTuple = ('apple','banana','melon')
print(thisTuple[1])

#Change tuple value
x=("1","a","3")
y=list(x)
y[1]=2
x=tuple(y)
print(x)

#Join tuple
joinTupleA = ('1','2','3')
joinTupleB = ('a', 'b','c')

joinTupleC = joinTupleA + joinTupleB
print(joinTupleC)

#Sets collection
thisset = {'apple','orange','banana'}
print(thisset)

#Add one item in sets collection
thisset.add('melon')
print(thisset)

#Add mutiple item to a set
thisset.update(["mango","grapes"])
print(thisset)

#Remove item
# => remove() => If item to remove does not exist, remove() will raise an error
# => discard() => If item to remove does not exist, discard() will NOT raise an error
thisset.remove('grapes')
print(thisset)

#Clear the set
#thisset.clear()
#print(thisset)

#Delete the set

#del thisset
#print(thisset)

#Join two set => Exclude any dupicate item
#Option 1: Using union() => Return a new set with all item from both sets
set1 = {"apple","banana","mango"}
set2 = {"zed","leesin","mango"}
set3 = set1.union(set2)
print(set3)
#Option 2: Using update() =>Insert item set2 into set1
set1.update(set2)
print(set1)

#Dictionaries Collection
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Accessing items
x = thisdict["year"]
y = thisdict.get("model")
print(x)
print(y)

#Change Value
thisdict["model"] = "DuyNND"
print(thisdict)

#Loop through a Dictionary
#Option 1: Print key name
for x in thisdict:
    print(x)
#Option 2: Print all values 
for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)
#Option 3: Get both key and value in dictionary
# =>Using items()
for x,y in thisdict.items():
    print(x, y)

#Adding items
thisdict["color"] = "red"
print(thisdict)

#Removing items
#Option 1: Using pop()
thisdict.pop("model")
print(thisdict)

#Coppy a Dictionary
mydict = thisdict.copy()
print(mydict)
