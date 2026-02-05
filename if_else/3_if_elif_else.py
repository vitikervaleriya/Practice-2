# The Elif Keyword

x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")

""""""""""""""""""""""""""""""""""""

score = 85
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")

""""""""""""""""""""""""""""""""""""

temperature = 25
if temperature > 30:
    print("It's hot")
elif temperature >= 20:
    print("It's warm")

""""""""""""""""""""""""""""""""""""

name = "Alice"
if name == "Bob":
    print("Hello Bob")
elif name == "Alice":
    print("Hello Alice")

""""""""""""""""""""""""""""""""""""

number = -5
if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")




# Multiple Elif Statements
temperature = 5
if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's warm")
elif temperature > 10:
    print("It's cool")
elif temperature >= 0:
    print("It's cold")

""""""""""""""""""""""""""""""""""""

age = 25
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 30:
    print("Young adult")
elif age < 50:
    print("Adult")

""""""""""""""""""""""""""""""""""""

score = 88
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Very Good")
elif score >= 70:
    print("Good")
elif score >= 60:
    print("Satisfactory")

""""""""""""""""""""""""""""""""""""

speed = 120
if speed > 150:
    print("Too fast")
elif speed > 120:
    print("Fast")
elif speed > 90:
    print("Moderate")
elif speed <= 90:
    print("Safe")

""""""""""""""""""""""""""""""""""""

points = 350
if points >= 500:
    print("Platinum member")
elif points >= 300:
    print("Gold member")
elif points >= 100:
    print("Silver member")
elif points >= 0:
    print("Bronze member")



# Complete If-Elif-Else Chain

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

""""""""""""""""""""""""""""""""""""

age = 17
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 30:
    print("Young adult")
else:
    print("Adult")

""""""""""""""""""""""""""""""""""""

speed = 95
if speed > 150:
    print("Too fast! Dangerous")
elif speed > 120:
    print("Fast")
elif speed > 90:
    print("Moderate")
else:
    print("Safe")
    
""""""""""""""""""""""""""""""""""""

points = 320
if points >= 500:
    print("Platinum member")
elif points >= 300:
    print("Gold member")
elif points >= 100:
    print("Silver member")
else:
    print("Bronze member")

""""""""""""""""""""""""""""""""""""

water_temp = 12
if water_temp > 30:
    print("Water is hot")
elif water_temp > 20:
    print("Water is warm")
elif water_temp > 10:
    print("Water is cool")
else:
    print("Water is cold")
