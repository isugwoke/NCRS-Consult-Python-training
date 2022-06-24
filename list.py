my_list = [1,'Two',3,4,5,6]

# List indexing
second_item = my_list[1]
print(second_item)

# List Slicing
first_3_items = my_list[1:3]
print(first_3_items)

# Concatenating list - use to join two or more lists together
list_1 = ['one', 'two', 'three']
list_2 = ['four', 'five', 'six']

all_list = list_1 + list_2
print(all_list)

# Mutating a list - Change the content of a list
my_list[5] = 'Six'
print(my_list)

# LIST METHODS
# append - Adds an item to the end of a list
my_list.append(7)
print(my_list)

# insert - inserts an item at a particular index
my_list.insert(3, 3.5)
print(my_list)

# pop - Removes an item from the end of a list
my_list.pop()
print(my_list)

my_list.pop(1) # Removes the item at index 1
print(my_list)

# sort - Sorts a list in ascending order

num_list = [3,2,1,4,6,7]
num_list.sort()

str_list = ['c', 'a', 'd']
str_list.sort()

print(num_list)
print(str_list)

# reverse - Reverses the items in a list
my_list = [1,2,3,4,5,6]

my_list.reverse()
print(my_list)

# sort descending order - Reverse trick
unsorted_list = [500, 100, 300, 200, 600]
unsorted_list.sort()
unsorted_list.reverse()

print(unsorted_list)
