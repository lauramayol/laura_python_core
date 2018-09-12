'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
    of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
    Print the results to the console.

    For example, if a user enters 1 and 100, the output should be:
        The sum is: 5050
        The average is: 50.5
'''
print("Enter lower number first: ")
lower = int(input())
print("Enter upper number next: ")
upper = int(input())


def calc_sum(l, u):
    sum_to_upper = 0
    while l <= u:
        sum_to_upper = sum_to_upper + l
        l += 1
    return str(sum_to_upper)


def calc_avg(l, u):
    avg = (l + u) / 2
    return str(avg)


print ("The sum is: " + calc_sum(lower, upper))
print ("The average is: " + calc_avg(lower, upper))
