from enum import Enum

# Ways to create constants in Python
class State(Enum):
  INACTIVE = 0
  ACTIVE = 1

print(State.ACTIVE.value)
print(State(1))

# print list of Enum
print(list(State))