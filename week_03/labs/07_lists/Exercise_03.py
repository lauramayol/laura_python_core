'''
Complete Exercise 10.1 (p.120) from the textbook.

Sum up all elements from a nested list of integers.

Exercise 10.1. Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21

'''


def nested_sum(t):
    num_sum = 0
    for num_list in t:
        num_sum = num_sum + sum(num_list)
    return num_sum


my_list = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(my_list))
