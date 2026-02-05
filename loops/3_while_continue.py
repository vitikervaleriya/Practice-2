# The continue Statement

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    
""""""""""""""""""""""""""""""""

numbers = [2, -1, 4, -3, 5]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1

""""""""""""""""""""""""""""""""

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

""""""""""""""""""""""""""""""""


words = ["hello", "", "world", "", "python"]
i = 0
while i < len(words):
    if words[i] == "":
        i += 1
        continue
    print(words[i])
    i += 1

""""""""""""""""""""""""""""""""

i = 0
while i < 8:
    i += 1
    if i > 5:
        continue
    print(i)
