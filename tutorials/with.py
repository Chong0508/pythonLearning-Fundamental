# With

# can help in open file

filename = 'tutorials/testFolder/text.txt'

with open(filename, 'r') as file:
  content = file.read()
  print(content)