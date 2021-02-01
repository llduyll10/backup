#Create Class
class MyClass: 
    x=5
print(MyClass)

#Create object
p1 = MyClass()
print(p1.x)

#__innit__() function
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("DuyNND",22)
print(p1.name)
print(p1.age)

#Object METHOD
#Object can also cotain method

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myFunction(self):
        print("Hello my name is: " + self.name)
p1 = People("DuyNguyenVJPPRO",20)
p1.myFunction()

#Self parameter
#parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
#Use the words mysillyobject and abc instead of self
class UpdatePerson:
    def __init__(duyobject,name,age):
        duyobject.name = name
        duyobject.age = age
    def myFunction(abc):
        print("Hello my name is: " + abc.name)
p1 = UpdatePerson("John", 30)
p1.myFunction()

#Delete Objects
# p2 = UpdatePerson("Test", 20)
# del p2.age
# print(p2.age)

#Python Inheritance

class ParentClass:
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname

    def printName(self):
        print(self.firstName, self.lastName)
P1 = ParentClass("Nguyen","Duy")
P1.printName()


#Create child class
class ChildClass(ParentClass):
    pass

P2 = ChildClass("Duy","Pro")
P2.printName()

#Add properties in Child class
#And add method in Child class
class People:
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
    def printName(self):
        print(self.firstName, self.lastName)

class Student(People):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year
    def welcomeNewbie(self):
        print(self.firstName, self.lastName, self.graduationyear)

x = Student("DuyNND","Vippro",2020)
x.welcomeNewbie()
print(x.graduationyear)