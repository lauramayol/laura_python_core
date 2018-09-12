'''
Complete Exercise 10.7 (p.121) - the birthday paradox - from the textbook.

Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.

'''


def has_duplicates(t):
    new_list = t[:]
    for x in t:
        del new_list[new_list.index(x)]
        if x in new_list:
            return True
    return False


my_list = [10, 20, 5, 31, 88, 31, 100, 87]
print(has_duplicates(my_list))
print(my_list)
