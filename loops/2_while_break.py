# The break Statement

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
    
""""""""""""""""""""""""""""""""

numbers = [5, 3, -1, 2]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        print("Negative number found, stop")
        break
    print(numbers[i])
    i += 1

""""""""""""""""""""""""""""""""


number = 0
while number < 10:
    number += 1
    if number == 7:
        print("Number 7 reached, stop loop")
        break
    print(number)

""""""""""""""""""""""""""""""""

fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    if fruits[i] == "banana":
        print("Found banana, break")
        break
    print(fruits[i])
    i += 1

""""""""""""""""""""""""""""""""

i = 5
while i > -1:
    if i == 0:
        print("Division by zero, stop")
        break
    print(10 / i)
    i -= 1
