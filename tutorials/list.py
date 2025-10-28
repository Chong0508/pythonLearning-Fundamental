dogs = ["Roger", 1, "Syd", True]

dogs[2] = "Jane" 

dogs.append("Mop")

dogs.extend(["Lion", 7])   # same as dogs += ["Lion", 7]

print(dogs)

print("Jane" in dogs)

print(dogs[1:3])

dogs.remove("Lion")

print(dogs.pop())    # .pop() remove the last element

print(dogs)

items = ["Mop", 1, "Syq", True]

items.insert(2, "Bow")
print(items)


# insert item between the index
items[1:1] = ["Test1", "Test2"]
print(items)

# sorting
# sort uppercase then lowercase
str1 = ["Mop", "Roger", "mop", "Jane"]

itemscopy = str1[:]
str1.sort()
print(str1)
print(itemscopy)

# sort no matter uppercase or lowercase
str2 = ["Mop", "Roger", "mop", "Aida"]
str2.sort(key=str.lower)     # same as sorted(str2, key = str.lower)
print(str2)


