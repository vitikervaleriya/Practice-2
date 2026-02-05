# The Else Keyword

x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("x is less than y")

"""""""""""""""""""""""""""""""""""" 

score = 75
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Grade C")

""""""""""""""""""""""""""""""""""""

temperature = 15
if temperature > 30:
    print("It's hot")
elif temperature >= 20:
    print("It's warm")
else:
    print("It's cold")

""""""""""""""""""""""""""""""""""""

name = "Alice"
if name == "Bob":
    print("Hello Bob")
elif name == "Alice":
    print("Hello Alice")
else:
    print("Hello stranger")

""""""""""""""""""""""""""""""""""""

items = ["apple", "banana"]
if not items:
    print("The list is empty")
elif len(items) == 1:
    print("One item in the list")
else:
    print("Multiple items in the list")




# Else Without Elif
x = 10
y = 20
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

""""""""""""""""""""""""""""""""""""

age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")

""""""""""""""""""""""""""""""""""""

password = "admin"
if password == "admin":
    print("Access granted")
else:
    print("Access denied")

""""""""""""""""""""""""""""""""""""

fruits = []
if fruits:
    print("The list has items")
else:
    print("The list is empty")

""""""""""""""""""""""""""""""""""""

number = -5
if number > 0:
    print("The number is positive")
else:
    print("The number is zero or negative")




# Else as Fallback

password = "secret123"
if len(password) >= 8:
    print("Password accepted")
else:
    print("Password too short")

""""""""""""""""""""""""""""""""""""

email = "user@example.com"
if "@" in email:
    print("Valid email address")
else:
    print("Invalid email address")

""""""""""""""""""""""""""""""""""""

items = ["apple", "banana"]
if items:
    print("Items available")
else:
    print("No items in stock")

""""""""""""""""""""""""""""""""""""

score = 85
if score >= 50:
    print("You passed the test")
else:
    print("You failed the test")

""""""""""""""""""""""""""""""""""""

temperature = 18
if temperature > 20:
    print("It's warm outside")
else:
    print("It's cool outside")
