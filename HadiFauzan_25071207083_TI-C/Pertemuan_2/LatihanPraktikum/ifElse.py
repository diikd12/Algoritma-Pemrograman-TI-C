#Else
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#Short Hand
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Logical Operators
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#nested if
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")
  
#pass statement
score = 85

if score > 90:
  pass # This is excellent
print("Score processed")