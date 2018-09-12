'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''
num = int(input())
check = 0
while check == 0:
    if num > 0 and num <= 1000000000:
        if num % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
        break
    else:
        print("Please enter a number between 1 and 1,000,000,000")
        num = int(input())
