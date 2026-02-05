# Python For Loops

colors = ["red", "green", "blue"]
for color in colors:
    print(color)

""""""""""""""""""""""""""""""""

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)

""""""""""""""""""""""""""""""""

word = "python"
for ch in word:
    print(ch)

""""""""""""""""""""""""""""""""

coordinates = (10, 20, 30)
for c in coordinates:
    print(c)

""""""""""""""""""""""""""""""""

student = {"name": "Alice", "age": 20}
for key in student:
    print(key)





# Looping Through a String

for ch in "apple":
    print(ch)

""""""""""""""""""""""""""""""""

word = "python"
for letter in word:
    print(letter)

""""""""""""""""""""""""""""""""

for c in "hi":
    print(c)

""""""""""""""""""""""""""""""""

for digit in "12345":
    print(digit)

""""""""""""""""""""""""""""""""

for symbol in "!@#":
    print(symbol)





# The range() Function

for x in range(5):
    print(x)

""""""""""""""""""""""""""""""""

for x in range(1, 6):
    print(x)

""""""""""""""""""""""""""""""""

for x in range(0, 10, 2):
    print(x)

""""""""""""""""""""""""""""""""

for x in range(10, 0, -1):
    print(x)

""""""""""""""""""""""""""""""""

for x in range(5, 51, 5):
    print(x)






# Else in For Loop

for x in range(3):
    print(x)
else:
    print("Loop completed")

""""""""""""""""""""""""""""""""

for x in range(5):
    if x == 2:
        break
    print(x)
else:
    print("Finished without break")

""""""""""""""""""""""""""""""""
numbers = [1, 3, 5, 7]
for n in numbers:
    if n == 5:
        print("Found 5")
        break
else:
    print("5 not found")

""""""""""""""""""""""""""""""""

numbers = [2, 4, 6]
for n in numbers:
    if n == 5:
        print("Found 5")
        break
else:
    print("5 not found")

""""""""""""""""""""""""""""""""

for ch in "python":
    print(ch)
else:
    print("All letters printed")






# Nested Loops

colors = ["black", "white"]
animals = ["cat", "dog"]

for c in colors:
  for a in animals:
    print(c, a)
""""""""""""""""""""""""""""""""

sizes = ["S", "M", "L"]
shirts = ["T-shirt", "Hoodie"]

for s in sizes:
  for sh in shirts:
    print(s, sh)
""""""""""""""""""""""""""""""""

numbers = [1, 2, 3]

for x in numbers:
  for y in numbers:
    print(x, y)
""""""""""""""""""""""""""""""""

names = ["Anna", "Bob"]
grades = ["A", "B", "C"]

for n in names:
  for g in grades:
    print(n, g)
""""""""""""""""""""""""""""""""

for i in range(1, 4):
  for j in range(1, 4):
    print(i, "*", j, "=", i * j)



# The pass Statement    

for x in range(5):
  pass

if True:
  pass

while False:
  pass

def my_function():
  pass

class MyClass:
  pass