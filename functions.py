# functions and methods

from itertools import product


def greet():
    sum = 100 + 200
    sum = sum + 2000
    half = sum / 2
    print(half)
    # print("Hello there")

# greet()

def greet_user(username):
    print("Good morning " + username)

# greet_user("Terfa")


def multiply(num1, num2, num3):
    product = num1 * num2 * num3
    print(product)

# multiply(2,4,2)

def calc_age(name, birth_year):
    age = 2022 - birth_year
    print(f"Good morning {name}, your age is {age}")

# calc_age('Linda', 1983)

# Returning a value from a function

def eval_age(birth_year):
    age = 2022 - birth_year
    return age

my_age = eval_age(1980)
# print(f"Hello, your age is {my_age}")

print(my_age)
age_ten_yrs_ago = my_age - 10
print(age_ten_yrs_ago)
