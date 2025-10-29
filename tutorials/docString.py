# Docstrings
# like comment (description)

"""Dog module

This module does ... bla bla bla and provides the 
following classes:

- Dog
...
"""

def increment(n):
  """Increment a number"""
  return n + 1

class Dog:
  """A class represent a dog"""
  def __init__(self, name, age):
    """Initialize a new dog"""
    self.name = name
    self.age = age
  
  def bark(self):
    """Let the dog bark"""
    print("WOF!")

print(help(Dog))