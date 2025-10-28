# Tuples
# Once created, cannot be modify (add or remove)

names = ("Roger", "Syd")

names[-1]   # returns from back  # Syd
names.index("Roger")  # 0

len(names)  # 2

print("Roger" in names)  # True

newTuple = names + ("Jane", "Tina")
