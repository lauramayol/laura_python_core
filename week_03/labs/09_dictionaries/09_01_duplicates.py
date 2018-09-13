'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.

Solution: http://thinkpython2.com/code/has_duplicates.py.

Source: Chapter "Dictionaries" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2011.html

'''


def make_dict(t):
    my_dict = dict()
    for x in t:
        if x in my_dict:
            my_dict[x] += 1
        else:
            my_dict[x] = 1
    return my_dict


def has_duplicates(t):
    my_new_dict = make_dict(t)
    for x in t:
        if my_new_dict[x] > 1:
            return True
    return False


my_list = [1, 5, 50, 23, 50, 100]
print(make_dict(my_list))
print(has_duplicates(my_list))
