# Double asterisk work as square
print(5**2)
# there can be cancetation also in the python
print(True+5)
# we cannot concatenate different types of data 
#  print("a"+5) - this is not possible as they are different types of data 


#output formatting
name,age,salary= "John", 28,48000.29
print("His name is: %s, and his age is %2d, and his salary is %g" % ("John",28,48000.29))


#another type of output formatting
print("Name is: {} age is {} and salary is {}".format(name,age,salary))


# type conversion

# -- converting string into integer using int()
num1 = int(input("Enter the first number: "))
# -- converting string into float using float()
num2 = int(input("Enter the second number: "))
sum = num1+num2
print(sum)