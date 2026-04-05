n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

print(f'The sum of the two numbers is {n1 + n2}.')

print(f'The result of multiplying {n1} and {n2} is {n1 * n2}.')

if n2 != 0:
    print(f'The result of dividing {n1} by {n2} is {n1 / n2}.')
else:
    print('Cannot divide by zero.')

print(f'The result of raising {n1} to {n2} is {n1 * n2}.')
