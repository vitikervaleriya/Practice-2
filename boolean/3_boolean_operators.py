#Functions can Return a Boolean

def is_empty():
    return False

print(is_empty())

""""""""""""""""""""""""

def is_even(n):
    return n % 2 == 0

print(is_even(4))

""""""""""""""""""""""""

def is_adult(age):
    return age >= 18

print(is_adult(16))

""""""""""""""""""""""""

def has_text(s):
    return bool(s)

print(has_text("Hello"))

""""""""""""""""""""""""

def is_integer(x):
    return isinstance(x, int)

print(is_integer(3.14))




#Logical Operators

x = 5
# AND
print(x > 0 and x < 10)        
print(x >= 5 and x <= 5)      
print(x > 3 and x < 4)        
print(x != 0 and x < 100)     
print(x > 10 and x < 20) 
# OR
print(x < 5 or x > 10)        
print(x == 5 or x == 0)       
print(x < 0 or x < 10)        
print(x > 100 or x == 5)      
print(x < 3 or x > 7) 
# NOT
print(not(x > 3 and x < 10)) 
print(not(x == 5))            
print(not(x < 0))             
print(not(x > 10))            
print(not(x != 5))   