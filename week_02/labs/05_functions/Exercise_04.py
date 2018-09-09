'''
Write a function that takes in a list and finds the max, min, average and sum.

'''


def list_calcs(x):
    print("The Max is: " + str(max(x)))
    print("The Min is: " + str(min(x)))
    print("The Sum is: " + str(sum(x)))
    print("The Average is: " + str(sum(x) / len(x)))


my_list = [1, 2, 3, 4, 51]

list_calcs(my_list)
