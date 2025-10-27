"Jane"
'Jane'

name = "Jane"
name += " is my name"
name2 = "Ja\"ne"
print(name)

# Multi-line print
print("""Jane is 

  18 

years old.
""")

# String method
print("Jane".upper())
print("jAne person".title())
print("jAne person".islower())
print(len(name))
print(name2)

# isalpha() to check if a string contains only characters and is not empty
# isalnum() to check of a string contains characters or digits and is not empty
# isdecimal() to check if a string contains digits and is not empty
# lower() to get a lowercase version of a string
# islower() to check if a string is lowercase
# upper() to get an uppercase version of a string
# isupper() to check if a string is uppercase
# title() to get a capitalized version of a string
# startswith() to check if the string starts with a specific substring
# endswith() to check if the string ends with a specific substring
# replace() to replace a part of a string
# split() to split a string on a specific character separator
# strip() to trim the whitespace from a string
# join() to append new letters to a string
# find() to find the position of a substring

# String slicing
print(name[1:3])
print(name[:3])
print(name[1:])
