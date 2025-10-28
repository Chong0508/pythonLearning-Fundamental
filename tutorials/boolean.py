done = True

if done:
  print("yes")
else:
  print("no")

# empty String return False
done2 = ""
done3 = "Jane"

if done2:
  print("yes2")
else:
  print("no2")

if done3:
  print("yes3")
else:
  print("no3")

# any : return true if either one is True
book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])

# all : return true if all is True
ingredients_purchased = True
meal_cooked = False
ready_to_serve = all([ingredients_purchased, meal_cooked])
