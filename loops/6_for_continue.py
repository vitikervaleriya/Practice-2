# The continue Statement

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 3:
        continue
    print(n)
    
""""""""""""""""""""""""""""""""

fruits = ["apple", "banana", "cherry"]
for f in fruits:
    if f == "banana":
        continue
    print(f)

""""""""""""""""""""""""""""""""

for x in range(6):
    if x % 2 == 0:
        continue
    print(x)

""""""""""""""""""""""""""""""""

words = ["hello", "", "world", ""]
for w in words:
    if w == "":
        continue
    print(w)

""""""""""""""""""""""""""""""""

numbers = [5, -1, 3, -2, 0]
for n in numbers:
    if n < 0:
        continue
    print(n)

