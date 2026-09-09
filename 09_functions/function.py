# *************************** Q:1 *****************************

# Q:1 - square ?

def square(param):
    return (param**2)

# print(square(5))

# *************************** Q:2 *****************************

# Q:2 - take two param and return sum ?

def sumN(num1,num2):
    return num1 + num2

# print(sumN(2,3))

# *************************** Q:3 *****************************

# Q:3 - polymorphism ?

def multiply(p1,p2):
    return p1 * p2

# print(multiply(23,"3"))

# *************************** Q:4 *****************************

# Q:4 - return multiple val ?

import math
def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return [area,math.floor(circumference)]

# print(circle(30))

# *************************** Q:5 *****************************

# Q:5 - greeting  ?

def greeting(name="john"):
    return "hello " + name

# print(greeting())

# *************************** Q:6 *****************************

# Q:6 - lambda  ?

cube = lambda x: x**3


# *************************** Q:7 *****************************

# Q:7 - sum all num  ?

def sum_all(*args):
    return sum(args)

# print(sum_all(1,3))

# *************************** Q:8 *****************************

# Q:8 - even generate  ?

def even_gen(limit):
    for i in range(2,limit+1,2):
        yield i


for num in even_gen(20):
     num
    # print(num)

# *************************** Q:9 *****************************

# Q:9 - recursive function  ?

def factorial(n):
    if n == 0:
        return 1
    else:
        num = n * factorial(n - 1)
        return num

hh =  factorial(4)    
print(hh,"hh")
