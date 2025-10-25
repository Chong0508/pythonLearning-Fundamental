# Arithmetic Operator
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16 (4 to the power of 2)
5 // 2 #2 (5 divide 2 equal 2.5 then rounding down to integer - floor division)

age = 8
age += 8
print(age)

# Concatenation
print("Scamp" + " is a good dog")

# Comparison Operator
a = 1
b = 2

a == b # False
a != b # True
a > b # False
a <= b # True

# Boolean Operator
condition1 = True
condition2 = False

not condition1 # False
condition1 and condition2 # False
condition1 or condition2 # True

# return first operand if 1st operand true, otherwise return second operand if 1st operand false
print(0 or 1) # 1
print(False or 'hey') # 'hey'
print('hi' or 'hey') # 'hi'
print([] or False) # 'False'
print(False or []) # '[]'

# only evaluate 2nd arguement if 1st is true, if 1st is false return 1st
print(0 and 1) # 0
print(1 and 0) # 0
print(False and 'hey') # False
print('hi' and 'hey') # 'hey'
print([] and False) # []
print(False and []) # False