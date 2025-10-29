# map(), filter(), reduce()

numbers = [1, 2, 3]

# map()
def double(a):       # same as double = lambda a : a * 2
  return a * 2

result = map(double, numbers)
print(list(result))

# filter()
def isEven(n):         # same as lambda n : n % 2 == 0
  return n % 2 == 0

result = filter(isEven, numbers)
print(list(result))

# reduce()
from functools import reduce

expenses = [
  ('Dinner', 80),
  ('Car repair', 120)
]
sum = reduce(lambda a, b : a[1] + b[1], expenses)

print(sum)