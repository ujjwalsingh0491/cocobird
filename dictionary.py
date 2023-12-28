# dictionary store the data in the form of key-value pair
# it is mutable but unordered, it has key-value indexing
# dictonary are pair of key-value pair & they are written in curly brackets
# key is always unique however value can be same for multiple keys 
mydictionary ={
    "brand": "Hyundai",
    "car":   "red",
    "airbags":  6
}
# it will print every key value pair
print(mydictionary)
# to print specific value we need to call the key in big bracket
print(mydictionary["brand"])
# we can also change values in the dictionary
mydictionary["car"] ="green"
print(mydictionary)

# we can also read values from the dictionary through for loop
# every key will be printed through the for loop
for i in mydictionary:
    print(i)

# to print the values we need to pass the index value in the mydictionary
for i in mydictionary:
    print(mydictionary[i])

# to print the key-value pair in separate lines we need to x,y in for loops
for x,y in mydictionary.items():
    print(x,y)

# we can also directly check whether a key is present in the dictionary or not
print("suzuki" in mydictionary)
print("airbags" in mydictionary)

# dictionary is mutable 
print(mydictionary)
# to add new key-value pair in mydictionary, specify the key name in big bracket and then its value 
mydictionary["license"]="data"
print(mydictionary)

# to add multiple items we have to write multiple items

# delete items in dictionary, using pop()
mydictionary.pop("car")
print(mydictionary)

mydictionary.pop('license')
print(mydictionary)

del mydictionary["airbags"]
print(mydictionary)

# pop() amd del() will return error if we try to delete the key that is not present in the dictionary
# mydictionary.pop('licensee')
# print(mydictionary)
# del mydictionary['rose']
# print(mydictionary)

# if we delete the mydictionary and try to print it then it will return the error
# del mydictionary
# print(mydictionary)

# in case we want to clear only contents and not the dictionary itself
mydictionary.clear()
print(mydictionary)

mydictionary2 = {1,2,3}

#copy() can be used to copy the content from one dictionary to another
mydictionary3 = mydictionary2.copy()
print(mydictionary3)
