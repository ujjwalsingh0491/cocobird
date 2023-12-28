# set is unordered and unindexed
# unordered means values are printed in any order 
# unindexed means we cannot apply loop on them

myset ={"apple","banana","cherry","strawberry"}
print(myset)
for i in myset:
    print(i)
# add can be used to add single element
myset.add("guava")
print(myset)

# update  can be used to add multiple elements 
myset.update(["pineapple"],["pancake"])
print(myset)
# len() is used to find the length of the myset
print(len(myset))

# remove() can be used to renove the value in tuple
myset.remove("banana")
print(myset)
# myset.remove("rose")
# print(myset)

# the difference between remove() and discard() is that when the element is not present and we use remove() it throws error while discard() doesn't throw such error
# myset.discard("rose")
# print(myset)

# clear() can be used to remove all the elements of the set 
myset2 = myset
# myset2.clear()
print(myset2)
print(myset)
# clear will remove all the element and blank set() is visible
# however when we use del keyword and try to print the set then set is deleted and error is displayed 
# myset3 = myset
# del myset3
# print(myset3)
set2= {2,3,4,"apple"}
myset4 = myset
print(myset4)
myset5 =myset4.union(set2)
print(myset5)


