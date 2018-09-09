'''
Using a "while" loop, find the sum of numbers from 1-100.
Print the sum to the console.

'''
lower = 1
sum_to_upper = 0

while lower <= 100:
    sum_to_upper = sum_to_upper + lower
    lower += 1

print ("The sum is: " + str(sum_to_upper))
