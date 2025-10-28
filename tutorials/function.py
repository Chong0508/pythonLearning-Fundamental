# Function

# required parameter
def hello(name, age):
  print("Hello! " + name + ", you are " + str(age) + " years old!")

hello("Jane", 18)

# optional parameter
def hello2(name = "my friend"):
  print("Hello! " + name)

hello2()

# include if statement
def hello3(name):
  if not name:
    return
  print("Hello " + name + "!")

hello3("Beau") 