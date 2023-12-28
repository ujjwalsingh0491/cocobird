# in java we have only methods 
# but in python we have both methods as well as functions and both are different things


# function is a group of statement that will perform certain task 
# main use of function is reusability, we just write function once and later can use that function as many times as we want

# there are two types of functions in the python - user defined and pre-defined functions (sum(),remove(),etc.)
# def is a keyword which is used to create a function
# creation and definition of the function
def hello_world():
    print("hello world")
# calling the function directly 
hello_world()


# function in the python can take arguments or paramters

def name(n):
    print("hello " + n)

name("cocobird")

# we can also multiple parameters in the function
def sum(a,b):
    print(a+b)

sum(3,6)

# when we use return statement and doesnot return anything then it will print None
def mul():
    return
print(mul())

def c():
    i=10
# it will print nothing on output console as we are neither printing anything not returning anything
print(c())


def cal(a,b):
    print(a+b)
# as we are not returning any thing so we don't need print() or any variable
cal(10,20)

# if the function is returning anything then we need any variable or print() to store the return value

# function can be created in 4 ways :
# 1. function with no arguments and no return value(none) 2. function with arguments but no return value
# 3. function with takes no arguments but return value 4. function takes arguments as well as return value

# In python we have two types of variables : 1. local variable 2. global variable
# variables created outside the function is global variable which can be used by any function
# variable created inside the function is local variable which can be used just inside the function

global_var =20 #global variable which can be used inside any function
def my_fun():
    print(global_var)
my_fun()

# global variable can be created before or after the function, but in case it is created after creating the function then it should be defined before calling the function

def my_fun1():
    print(global_var1)
global_var1=22
my_fun1()

# global and local variable can have same name but priority is always given to local variable
global_value = 23
def value():
    global_value=24
    print(global_value)
value()

# we can access the global variable inside the function even when its name is similar to the local variable
xyz = 250
def cools():
    # we can use global keyword to access the global variable inside the function
    global xyz
    xyz = 150
    # still the local variable will be printed 
    print(xyz)
cools()

b = 300
def cool():
    global b
    # global b = 100 is invalid, 
    b = 100
    print(b)
cool()


x = 12
def a():
    global x
    x=500
    print(x)
print(x)

def abc():
    global y
    y=72
    print(y)
abc()

# parameter or arguments in function are of two types 
# positional argument or parameter
# keyword argument or parameter

def func(i,j):
    print(i,j)
# this is positional argument as 10 will go to i and 20 will go to the j
func(10,20)
def func1(a,b):
    print(a,b)
# this is keyword argument where we are explicitly assigning values using variable names
func1(a=20,b=22)

def func3(i,j=10):
    print(i,j)
func3(70,80)

def func4(x,y=10):
    print(x,y)
func4(17)


#keyword arguments 
def greetings(name,greeting):
    print(greeting+" ",name)

greetings(greeting="Hi",name ="Angry Bird")

def my_func(a,b,c):
    print(a,b,c)
# this will work because even though a,b,c are not in order but still we are explicitly assigning value to each of them
my_func(a=10,c=25,b=36)
# even though the below line is a combination of positional and keyword argument still it will work because positional argument is followed by keyword argument
my_func(42,13,c=98)
# similarly below line is also valid 
my_func(38,b=12,c=23)
# positional argument must always come before the keyword argument else it will throw error
# my_func(40,b=23,19)

# this will throw error of "Multiple Assignment of b"
# my_func(26,43,b=21)

# my_func(12,c=17,23)



def largest(a,b):
    if a>b:
        return a
    else:
        return b

print(largest(100,200))
# if the function is returning multiple value then the result is of tuple type

