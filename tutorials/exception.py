# Exceptions

# Example 1
try:
  result = 2 / 0
except ZeroDivisionError:
  print('Cannot divide by zero!')
finally:
  result = 1

print(result)   # 1

# Example 2
try:
  raise Exception('An error!')
except Exception as error:
  print(error)


# Example 3
class DogNotFoundException(Exception):
  print("inside")
  pass

try:
  raise DogNotFoundException()
except DogNotFoundException:
  print("Dog not found!")
