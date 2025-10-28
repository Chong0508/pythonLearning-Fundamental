# Dictionaries

dog = { "name": "Roger", "age": 8, "color": "green"}

dog["name"] = "Syd"

print(dog["name"])
print(dog.get("name"))
print(dog.get("color"))
print(dog.get("color", "brown"))

print("color" in dog)

# Remove element
print(dog.pop("name"))
print(dog)

# Remove last element
print(dog.popitem())
print(dog)

# display all keys
print(dog.keys())
print(list(dog.keys())) 

# display all values
print(dog.values())

# display all
print(list(dog.items()))

dog["favourite food"] = "Meat"

# length 
print(len(dog))

# reomve element
del dog["age"]
print(dog)