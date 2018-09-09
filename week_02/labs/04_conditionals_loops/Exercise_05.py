'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
    of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
    Print the results to the console.

    For example, if a user enters 1 and 100, the output should be:
        The sum is: 5050
        The average is: 50.5
'''
lower = int(input())
upper = int(input())

sum_to_upper = 0
avg = (lower + upper) / 2

while lower <= upper:
    sum_to_upper = sum_to_upper + lower
    lower += 1

print ("The sum is: " + str(sum_to_upper))
print ("The average is: " + str(avg))
