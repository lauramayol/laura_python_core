'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''


def my_enumerate(t):
    enum_list = list()
    for x in range(len(t)):
        tup = tuple()
        tup = x, t[x]
        enum_list.append(tup)
    return enum_list


my_list = ["cake", "wine", "school", "videochat", "birthday"]

print(my_enumerate(my_list))

for index, value in enumerate(my_list):
    print(index, value)
