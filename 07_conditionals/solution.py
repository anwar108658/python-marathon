# *************************** Q:1 *****************************

# Q:1 - age group categories ?


# age = 18

# if  age < 13:
#         print("child")
# elif age < 19:
#         print("teenage")
# elif age < 60:
#         print("adult")
# else:
#         print("senior")


# *************************** Q:2 *****************************

# Q:2 - movie ticket price are based on age 

age2 = 20
day = "wednesday"
price = None

if(age2 >= 18):
    price = 12
else:
    price = 8

if day == "wednesday":
    price -= 2

# print(price)



# *************************** Q:3 *****************************

# Q:3 - Grad calculator

score = 75
grade = None

if score >= 90:
    grade="A+"
elif score >= 80:
    grade="A"
elif score >= 70:
    grade="B"
elif score >= 60:
    grade="C"
elif score >= 50:
    grade="D"
elif score >= 40:
    grade="E"
else:
    grade="F"

# print(grade)


# *************************** Q:4 *****************************

# Q:4 - Fruit Ripeness Checker

color = "green"
fruit = "banana"
fruitStatus = ""

if fruit == "banana":
    if color == "green":
        fruitStatus="Unripe"
    elif color == "yellow":
        fruitStatus="Ripe"
    else:
        fruitStatus="Overripe"

# print(fruitStatus)

# *************************** Q:5 *****************************

# Q:5 - Weather Activity Suggestion

weather = "Sunny"
activity = None

if weather == "Sunny":
    activity="Go for a walk"
elif weather == "Rainy":
    activity="Read a book"
elif weather == "Snowy":
    activity="Build a snowman"

# print(activity)


# *************************** Q:6 *****************************

# Q:6 - suggestion based on distance

distance = 1.5
suggestion = None

if distance < 3:
    suggestion="walk"
elif distance < 15:
    suggestion="bike"
elif distance > 15 :
    suggestion="car"

# print(suggestion)

# *************************** Q:7 *****************************

# Q:7 - suggestion based on distance

year = 2027

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year , "is a Leap Year")
else:
    print(year , "is not a Leap Year")