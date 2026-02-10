# assignment operators
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#comparison operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#logical operators
x = 5

print(x > 0 and x < 10)

x = 5

print(not(x > 3 and x < 10))

#Identity operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#Membership operators
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#Bitwise operators

print(6 & 3)

#Precedences Operators
print(5 + 4 - 7 + 3)