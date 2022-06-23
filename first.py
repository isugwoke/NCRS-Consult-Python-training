a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

# x = -b +- the squareroot of b2 - 4ac all divided by 2a

d = b**2 - (4*a*c)

x1 = (-b + d**0.5) / (2*a)
x2 = (-b - d**0.5) / (2*a)

x1 = round(x1,2)
x2 = round(x2,2)

print(f'x = {x1}, x = {x2}')

# result = 10/3

# print('The Result is: {r:1.2f}'.format(r=result))


# result = 10/3
# print(round(result, 2))

# print(round(2.333333333, 2))