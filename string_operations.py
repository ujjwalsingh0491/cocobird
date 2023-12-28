string = "You are welcome"
# islower checks if the string is only lower character
# isupper checks if the string is only upper character
print(string.islower())
print(string.isupper())

#isalnum checks if the string contains only number
print(string.isalnum())

#isalpha checks if the string contains only alphabet
print(string.isalpha())
string1 = "Youarewelcome"
print(string1.isalpha())
string2 = "2"
# isdigit checks whether there is digit or not in the string
print(string2.isdigit())

# isidentifier checks whether there is any reserved word or not in the list
print(string.isidentifier())

#isSpace checks whether there is any space in the string or not
print(string1.isspace())
print(string.isspace())
a =" "
print(a.isspace())

# endswith check whether the string ends with the particular sub string or not
print(string.endswith("come"))

# startswith check whether the string starts with the particular string or not
print(string.startswith("You"))

#find() will check if the sub-string is present in the string or not
print(string.find("are"))
print(string.find("bde"))

# count will return the number the character is repeated in the string
print(string.count("e"))

# capitalize() will capitalize the first character of first word of the string
a=string.capitalize()
print(a)
# title() will capitalize the every starting character of every word in the string
print(string.title())

# lower will change every character to lower case
print(string.lower())
#similarly upper() will change every character to upper case
print(string.upper())

# swapcase will change the character from the existing to the opposite one
print(string.swapcase())
# replace will replace the string or sub-string with the new string or sub string
print(string.replace("are","is"))

# reverse a string
s2 = "welcome"
i= ""
rev_str = s2[::-1]
print(rev_str)
# s3 ="welcome"
# rev_str2=""
# for i in s3:
#     rev_str2=rev_str2+i

# print(rev_str2(s3))


