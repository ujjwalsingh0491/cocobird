a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else:
    print("a is equal to b")


# range is used in loop to consider a range of values
for i in range(1,10,1):
    print(i)

for i in range(11,1,-1):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(12,3,-1):
    print(i)

# printing list of values using list function

print(list(range(10)))
print(list(range(1,43)))
print(list(range(1,10,2)))
print(list(range(12,2,-2)))


# while loop
i=1
while(i<10):
    print(i)
    i+=1

# for i in range(2,-2,-1):
#     print(4/i)
#     if i==0:
#         break

for i in range(5,1,-1):
    a=i/1
    if a==3:
        continue
    else:
        print(a)

# max() and min() will return the maximum and minimum value in the list of numbers
print(max(5,3))

a = ""
print(id(a))

a = a+ " writing is on the wall"
print(a)
print(id(a))

str= "Welcome"
print(str+" to the...")


# slicing 
str3 ="welcome"
# it will print only 1st and 2nd character of the string
print(str3[1:3])
print(str3[:6])
print(str3[2:])
print(str3[:-1])
# ord will print ASCII value of the character mentioned in ord()
print(ord("A"))
# chr will print the character corresponding to the number mentioned in chr()
print(chr(65))
# max() with string will return the character in the string having maximum value
print(max("abc"))
# similarly min() with string will return the character in the string having minimum value
print(min("ghfiguergbgugr"))

# we can do string comparison also in the python
print("tim"=="tim")
print("tim"=="tie")
