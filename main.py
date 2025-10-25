name = "Jane"
print(type(name))
print(type(name) == str)
print(isinstance(name, str))

age = 2
print(isinstance(age, int))
print(isinstance(age, float))

age2 = float(2)
print(isinstance(age2, float))

age3 = "20"
age4 = int("20")
print(isinstance(age3, int))
print(isinstance(age4, int))
