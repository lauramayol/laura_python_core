'''
Complete Exercise 10.3 (p.121) from the textbook.


Exercise 10.3. Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]

'''


def middle(t):
    new_list = t[1:-1]
    return new_list


my_list = [1, 2, 3, 4, 5, 10, 12]
print(middle(my_list))
print(my_list)
