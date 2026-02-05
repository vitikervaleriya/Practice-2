# Short Hand If

a = 5
b = 2
if a > b: print("a is greater than b")

""""""""""""""""""""""""""""""""""""

username = "Alice"
if username: print(f"Hello, {username}!")

""""""""""""""""""""""""""""""""""""

fruits = ["apple", "banana"]
if fruits: print("The list has items")

""""""""""""""""""""""""""""""""""""

is_logged_in = True
if is_logged_in: print("User is logged in")

""""""""""""""""""""""""""""""""""""

number = 8
if number % 2 == 0: print("The number is even")





# Short Hand If ... Else

a = 2
b = 330
print("A") if a > b else print("B")

""""""""""""""""""""""""""""""""""""

age = 18
print("Adult") if age >= 18 else print("Minor")

""""""""""""""""""""""""""""""""""""

username = ""
print("Welcome!") if username else print("No username provided")

""""""""""""""""""""""""""""""""""""

number = 7
print("Even") if number % 2 == 0 else print("Odd")

""""""""""""""""""""""""""""""""""""

fruits = []
print("Has items") if fruits else print("List is empty")





# Assign a Value With If ... Else

x = 5
y = 8
smaller = x if x < y else y
print("Smaller is", smaller)

""""""""""""""""""""""""""""""""""""

number = 7
parity = "Even" if number % 2 == 0 else "Odd"
print(parity)

""""""""""""""""""""""""""""""""""""

name = ""
status = "Has name" if name else "No name"
print(status)

""""""""""""""""""""""""""""""""""""

a = 10
b = 15
c = 12
max_num = a if a > b else b
max_num = max_num if max_num > c else c
print("Maximum number is", max_num)

""""""""""""""""""""""""""""""""""""

temperature = 18
message = "Warm" if temperature > 20 else "Cool"
print(message)





# Multiple Conditions on One Line

x = 10
y = 5
print("X") if x > y else print("=") if x == y else print("Y")

""""""""""""""""""""""""""""""""""""

score = 85
print("A") if score >= 90 else print("B") if score >= 75 else print("C")

""""""""""""""""""""""""""""""""""""

temperature = 15
print("Hot") if temperature > 25 else print("Warm") if temperature > 15 else print("Cold")

""""""""""""""""""""""""""""""""""""

age = 12
print("Child") if age < 13 else print("Teen") if age < 20 else print("Adult")

""""""""""""""""""""""""""""""""""""

number = 7
print("Even") if number % 2 == 0 else print("Odd") if number % 2 != 0 else print("Zero")
