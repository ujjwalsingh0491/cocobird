# list can hold multiple values 
a =[10,12,13,14,15,16]

# list can hold multiple values of different data types
a1 = [10,"b",12.12,0.58438]
print(a)
print(a1)
# list can be added as usual
a2 = a+a1
print(a2)
# below line will print only two values, second and third value of the list
print(a2[1:3])
# the last character has the position of -1 and then from right to left it keeps decreasing
# -4 is the 4th character from the left to the last character
print(a1[-4:-1])


# list is mutable hence we can replace any element of the list with a new element
a2[0] = 14
print(a2)

# loop can be used to print multiple elements of list 

for i in range(0,len(a2),1):
    print(a2[i],end=" ")
# append is used to add element at the last of the list
a2.append("orange")
print(a2)
a3 = a2
# clear() will clear all the values and empty big brackets are visible on the screen
a3.clear()
print(a3)
a5 = [10,6,7,8,9,13,14,15,16,17]
a6 = list(a5)
print(a6)
a7 = a5.copy()
print(a7)

# we can also append list through for loop
list1 = ["a",17,19,20.123]
list2 = ["apple","banana","cherry"]
for i in list2:
    list1.append(i)
print(list1)

# we can also add element in the list through extend()
list3 = ["a","b","c","d","e"]
list4 =[1,2,3]
list3.extend(list4)
print(list3)

list3.pop(3)
print(list3)
del list3[2]
print(list3)

