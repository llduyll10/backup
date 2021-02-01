def my_function():
    print("Hello world!")

my_function()

#Fucntio with parameter
def param_fucntion(name):
    print("Hello " + name)
param_fucntion("DuyNND")

#Default parameter value
def default_value_function(name="Default DuyNND "):
    print("Hello " + name)
default_value_function()

#Lambda
x = lambda a: a+10
print(x(5))

#Using when yout use them as an anonymous function inside another function
def myLambdaFunc(n):
    return lambda a: a*n
mydoubler = myLambdaFunc(3)
print(mydoubler(10))