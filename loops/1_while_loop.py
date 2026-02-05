# The while Loop

i = 1
while i < 6:
    print(i)
    i += 1

""""""""""""""""""""""""""""""""

i = 5
while i > 0:
    print(i)
    i -= 1

""""""""""""""""""""""""""""""""

i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Total:", total)

""""""""""""""""""""""""""""""""

fruits = ["apple", "banana", "cherry"]
while fruits:
    fruit = fruits.pop(0)
    print(fruit)

""""""""""""""""""""""""""""""""

number = 0
while number <= 0:
    number = int(input("Enter a positive number: "))
print("You entered:", number)





# The else Statement

i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("Loop finished")
    
""""""""""""""""""""""""""""""""

i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print("Countdown complete")

""""""""""""""""""""""""""""""""

i = 1
total = 0
while i <= 3:
    total += i
    i += 1
else:
    print("Sum is", total)

""""""""""""""""""""""""""""""""

fruits = ["apple", "banana", "cherry"]
while fruits:
    fruit = fruits.pop(0)
    print(fruit)
else:
    print("All fruits removed")

""""""""""""""""""""""""""""""""

number = -1
while number <= 0:
    number = int(input("Enter a positive number: "))
else:
    print("Thank you! You entered:", number)
