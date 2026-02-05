# Boolean Values

print(1 > 2)
print(5 == 5)
print(9 < 10)
print(3 >= 100)
print(93 <= 99)



a = 10
b = 5
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

""""""""""""""""""""""""

password = "admin"
if password == "admin":
    print("Access granted")
else:
    print("Access denied")

""""""""""""""""""""""""

is_logged_in = True
if is_logged_in:
    print("User is logged in")
else:
    print("User is not logged in")

""""""""""""""""""""""""

items = ["apple", "banana"]
if items:
    print("The list has items")
else:
    print("The list is empty")

""""""""""""""""""""""""

number = 0
if bool(number):
    print("Number is not zero")
else:
    print("Number is zero")


#Evaluate Values and Variables
print(bool("Python"))      
print(bool(""))            
print(bool(0))           
print(bool(42))            
print(bool([1, 2, 3])) 


#Most Values are True

print(bool("hello"))           
print(bool(1))                 
print(bool(3.14))               
print(bool((1, 2)))            
print(bool({"a": 1, "b": 2}))


#Some Values are False

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})




