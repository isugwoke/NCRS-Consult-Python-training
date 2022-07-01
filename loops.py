# for loop 
# while loop

from itertools import product


my_list = [1,2,3,4,5,6,7]
# for loop

# syntax: for item in an_iterable:
    # do something

# for item in my_list:
    # print(item)

# sum up the numbers in the list
sum = 0;

for num in my_list:
    sum = sum + num; # 0 + 1, 2 +2, 4+3, 7+4, ....

# print(sum)

my_str = "NCRS Consult"

# for char in my_str:
    # print(char)

my_list2 = [1,2,3,4,5,6,7,8,9,10]


# for num in my_list2:
#     # product = 2 * num
#     print(2 * num)

# Print the even numbers in the list
for num in my_list2:
    if(num % 2 == 0):
        print(num)
    else:
        print("ODD")

# Loop throug a list of numbers and push the number into a new list if it is even
# even_nums = []



# While loops
# Repeat action(s) as long as the condition is true

a = 2
while a < 5:
    print('It is less than 5')
    a = a + 1









