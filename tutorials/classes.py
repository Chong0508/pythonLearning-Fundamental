# classes

class Animal:
  def walk(self):
    print("Walking...")

# Dog class inherent from Animal class
class Dog(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print("woof!")

roger = Dog("Roger", 8)
print(type(roger))
print(roger.name)
print(roger.age)

roger.bark()
roger.walk()