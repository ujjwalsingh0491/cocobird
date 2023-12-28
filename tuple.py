# tuple is collection which is ordered and immutable(unchangeable)
mytuple = ("apple","banana","cherry","strawberry")
print(mytuple)

# tuple is immutable so it is more secure than list
print(mytuple[-1])
print(mytuple[-2])

print(mytuple[1:2])
 # neither an element can be added, nor removed nor appended

 # to modify the tuple we need to first change it to the list and then modify it and again change it to list

mylist = list(mytuple)
mylist[2]="guava" 
mytuple = tuple(mylist)
print(mytuple)


for i in mytuple:
    print(i)
tuple1 =("a","b","c")
tuple2 =("apple","banana","cherry")
# tuples can be added 
tuple3 = tuple1+tuple2
print(tuple3)

