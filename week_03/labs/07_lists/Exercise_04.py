'''
Complete Exercise 10.2 (p.120) from the textbook.

Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumu- lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]

'''


def cumsum(t):
    cum_list = list()
    num_sum = 0
    for num in t:
        num_sum += num
        cum_list.append(num_sum)
    return cum_list


my_list = [10, 2, 3]
print(cumsum(my_list))
