'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''
lower = int(input())
upper = int(input())


for x in range(lower, upper):
    print(x ** 2)
