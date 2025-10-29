# Loops

# Example 1
condition = True
while condition == True:
  print("The condition is True")
  condition = False

# Example 2
count = 0
while count < 10:
  print("The condition is True")
  count = count + 1

print("After the loop")

# Example 3
items = [1, 2, 3, 4]
for item in items:
  print(item)

for index, item in enumerate(items):
  print(index, item)

# Example 4
# range(number) 
for item in range(15):
  print(item)

# Break - Stop the loop
items = [1, 2, 3, 4]
for item in items:
  if item == 2:
    break
  print(item)

# Continue - Miss the iteration, then continue next iteration
items = [1, 2, 3, 4]
for item in items:
  if item == 2:
    continue
  print(item)