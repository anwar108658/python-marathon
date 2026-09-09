# *************************** Q:1 *****************************

# Q:1 - how many are positive ?

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1

# print(positive_number_count)

# *************************** Q:2 *****************************

# Q:2 - calculate sum of even ?

n = 10
sum_even = 0

for i in range(n):
    if i % 2 == 0:
        sum_even += 1

# print(sum_even)

# *************************** Q:3 *****************************

# Q:3 - multiplication of table ?

table = 5

for i in range(1,11):
    if i == 5:
        continue
    # print(table , " x " , i , " = " , table * i)

# *************************** Q:4 *****************************

# Q:4 - Reverse a string using a loop ?

input_str = "hello world"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str


# print(reversed_str)

# *************************** Q:5 *****************************

# Q:5 - Reverse a string using a loop ?

input_str1 = "teeter"

for char in input_str1:
    if input_str1.count(char) == 1:
        # print("char is" ,char)
        break

# *************************** Q:6 *****************************

# Q:6 - factorial calculate ?

number = 4
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1

# print("factorial",factorial)

# *************************** Q:7 *****************************

# Q:7 - user_input b/w 1 to 10 ?

while True:
    # num = int(input("num btw 1 to 10 : "))
    if  1 <= num <= 10:
        # print("hello")
        break
    else:
        # print("invalid")
        break

# *************************** Q:8 *****************************

# Q:8 - prime number ?


number2 = 6

is_prime = True

if number2 > 1:
    for i in range(2,number2):
        if number2 % i == 0:
            is_prime = False
            break

# print(is_prime)

# *************************** Q:9 *****************************

# Q:9 - unique item checker ?

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for i in items:
    if i in unique_item:
        # print("duplicate")
        break
    else:
        unique_item.add(i)

# *************************** Q:10 *****************************

# Q:10 - wait  ?
import time

wait_time = 1
max_try = 6
attempts = 0

while attempts < max_try:
    print("wait for ",wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
    