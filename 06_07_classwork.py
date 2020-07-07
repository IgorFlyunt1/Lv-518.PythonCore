#task 1

a = int(input('Number 1'))
b = int(input('Number 2'))

if a > b:
    print('Number 1> Number 2')
else:
        print('Number 1 < Number 2')


#task 2

a = int(input('Enter number'))

if a % 2 == 0:
    print('Entered number is even')
else:
    print('Entered number is not even')


#task 3

n = int(input('enter number'))
a = 1
for i in range(2,n+1):
    a = a * i
    print('factorial is :', a)

#or

import math
n = int(input('enter number'))
print(math.factorial(n))
