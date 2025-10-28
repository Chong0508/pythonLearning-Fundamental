# Nested Function

# Example 1
def talk(phrase):
  def say(word):
    print(word)

  words = phrase.split(' ')
  for word in words:
    say(word)

talk("I am going to buy the milk")

# Example 2
def counter():
  count = 0

  def increment():
    nonlocal count
    count = count + 1
    return count

  return increment

increment = counter()

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3

