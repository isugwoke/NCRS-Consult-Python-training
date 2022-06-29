# Request details from the user
f_name = input("Enter your first Name: ")
m_name = input("Enter your Middle Name: ")
l_name= input("Enter your Last Name:")
birth_year = int(input("enter your Birth Year:"))


# Calculate current age
age = 2022 - birth_year;

# grab the first letters and convert to upper case
first_init = f_name[0].upper()
second_init = m_name[0].upper()

# Evaluate the users initials
initials = first_init+ "." + second_init

#  "Hello, MJ Okoh, you were born in 1979, you are currently 43 years old"

# print the final statement
print(f"Hello, {initials} {l_name} you were born in {birth_year}, you are currently {age} years old")









