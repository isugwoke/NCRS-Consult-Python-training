# Three conditional statements in python
# 1. if
# 2. elif
# 3. else

a = 2

# if a == 20:
#     print("Yes a is equal to 20")
# else:
#     print('No!!, a is not equal to 20')

# age_group = input('Enter your age group: ')

# if age_group == 'child':
#     print("You can only have a juice")
# elif age_group == 'teenager':
#     print('You can have water and juice')
# elif age_group == 'adult':
#     print('You can have a beer')
# else: 
#     print('We dont know your age group. go home!')

# age = int(input("Enter your age: "))

# if age > 1 and age < 13:
#     print("You are a child")
# elif age >12 and age < 20:
#     print("You are a teenager")
# elif age > 20:
#     print("You are an adult")
# else:
#     print("You have entered an inalid age: enter a number greater 1:")

num1 = 1000
num2 = 500

action = input("What do you want to do? Enter 1 to add or 2 to subtract: ")

if action == '1':
    sum = num1 + num2
    print(f"Sum of the 2 numbers is: {sum} ")

elif action == '2':
    diff = num1 - num2
    print(f"The difference btw the 2 numbers is: {diff}")

else:
    print("Invalid input. Please enter 1 or 2")