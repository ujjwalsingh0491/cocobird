# python support structured as well as object oriented programming language
# features that a programming language should have for supporting oops--
# 1. class 2. object 3. polymorphism 4. inheritance
# class is a logical entity whereas object is a physical entity
# class - employee , object - employee name, address, etc.
# class - animal , object - dog,horse,elephant,etc. 

# class is a collection of variables(attributes) and methods(behaviour)
# in employee management system - employee name is a variable as it vary from employee to employee while bonus is used to calculate the bonus of every employee so that will be methods
# class contains methods and variables
# class is blue print,logical entity and doesnot occupy memory 
# object is actual thing, physical entity and occupy memory 
# once class is created we can create multiple objects to call the variables and methods of class
# as soon as any object is created, all the variables and methods are copied into it and they occupy memory
# every object is independent of each other even though they share common variables and methods 

# method is similar to the function in python however both are bit different as methods can be created inside the class and function can be created outside the class
# method is created within the class so it is dependent on class however as function is created outside the class so it is independent of the class
# methods and variables are optional in class so we can create class without these things also

# whenever we create methods inside class self word is added by default as argument as it implies that the methods belong to this class 
# in case we don't want to add any operation in method we can use the keyword pass in the method 
# indentation is important while creating the class 

class myfun:
    def my(self):
        pass

class name:
    def nam(self,namee):
        print(namee)
a = name()
a.nam("cocobird")
a1 =name()
a1.nam("angrybird")

# a and a1 are different objects so they will occupy different memory space as even though they use same variable and attribute
# below line will throw error as ujjwal will go to the self, however namee will expect a argument
# a2 = name.nam("ujjwal")

# there are two different types of methods - instance method and static method 
# in the instance method - self refers to the class whereas in the static method self refers to the argument
a2=name.nam(100,200)

# class variable - when we create variable within class it is called class variable 
class name2:
    a,b =10,20
    def add(self):
        # below line will throw error as a and b are class variable not global variable
        # print(a,b)

        # so to access the class variable we need to use the self keyword
        print(self.a,self.b)
name22 = name2()
name22.add()

class name3:
    a,b =10,20
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)
name33 = name3()
name33.add()
name33.mul()

i,j =12,17  #this is global variable, declaring the variable before the class declaration
class name4:
    p,q = 15,20     # this is class variable as we are declaring and defining the variable within class
    def add(self,x,y):             # this is local variable as we are creating variable inside the methods
        print(self.p+self.q) # accessing the class variable with self keyword
        print(x+y)           # accessing the local variable directly
        print(i+j)           # accessing the global variable directly

name44 = name4()
name44.add(6,7)              # passing values as arguments for x and y

# global, class and local variable can be same, however to access each of them we have to use separate methods

u,v = 17,19
class name5:
    u,v = 20,23
    def add(self,u,v):
        print(u+v)
        print(self.u+self.v)
        print(globals()['u']+globals()['v'])

name55 = name5()
name55.add(10,15)


# method and constructor have few differences 
# method can have any name, method can take any number of paramters and methods need objects for to be called
# bydeafult constructor in the python will have name in the format __init__(self) keyword
# we don't need to call the constuctor explicitly by using the object, once the object is created the constructor is itself created 

class name6:
    def __init__(self) -> None:
        print("This is constructor")
    def hello():
        print("Hello ")
name66 = name6()
name6.hello()

class name7:
    def __init__(self) -> None:
        print("This is constructor 2")
    def add(self,x,y):
        print(x+y)
    def mul(self,x,y):
        print(x*y)
name77 = name7()
name77.add(10,15)
name77.mul(10,15)

class name8:
    def __init__(self,name) -> None:      # name is local variable for constructor
        print("Hello "+name)
# name88 = name8() -- this will not work as the constructor will be expecting a argument for name variable 
# below line will work, as we are passing a value which will be assigned to the name variable 

name88 = name8("rocky")

class name9:
    name = "flower"
    def __init__(self) -> None:
        print(self.name)
name99 = name9()

class emp:
    
    def __init__(self,eid,ename,esal) -> None:
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def display(self):
        print("Name is {} ,his id is {} and his salary is {}".format(self.eid,self.ename,self.esal))
em = emp(100,"cocobird",50000)
em.display()

# we can create second constructor also but that will work for string only and not the integer

class emp1:
    
    def __init__(self,eid,ename,esal) -> None:
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def __str__(self,age) -> str:
        return self.age
    def display(self):
        print("Name is {} ,his id is {} and his salary is {} and also his name is {} and age is {}".format(self.eid,self.ename,self.esal,self.age))
# the second constructor will return string type value and that too only single value, it will neither return integer type nor multiple value
emp = emp1(10,"angrybird",1)

emp.display()



