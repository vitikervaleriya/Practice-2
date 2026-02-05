# The break Statement

numbers = [1, 3, 5, 7]
for n in numbers:
    print(n)
    if n == 5:
        break

""""""""""""""""""""""""""""""""

numbers = [2, 4, 6, 8]
for n in numbers:
    if n == 6:
        break
    print(n)

""""""""""""""""""""""""""""""""

word = "banana"
for ch in word:
    if ch == "n":
        break
    print(ch)

""""""""""""""""""""""""""""""""
i = 0
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1

""""""""""""""""""""""""""""""""

fruits = ["apple", "orange", "banana", "cherry"]
for f in fruits:
    if f == "banana":
        print("Found banana, stop loop")
        break
    print(f)

