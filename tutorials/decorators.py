# Decorators

def logtime(func):
  def wrapper():
    # do something before
    print("before")
    val = func()
    # do something after
    print("after")
    return val
  return wrapper

@logtime
def hello():
  print("Hello")

hello()