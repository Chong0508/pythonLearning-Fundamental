# Sets
# Sets will ensure only one same item exist

set1 = {"Roger", "Syd", "Roger"}
set2 = {"Roger", "Tina"}

print(set1)

intersect = set1 & set2
print(intersect)

mod = set1 | set2
print(mod)

mod1 = set1 - set2
print(mod1)

mod2 = set1 > set2
print(mod2)

print(list(set1))