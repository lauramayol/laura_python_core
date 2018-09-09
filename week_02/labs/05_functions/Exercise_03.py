'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def concat_delim(word, delim):
    message = word + delim + word
    return message


def print_z(wordz, z, delimz):
    message = ""
    for y in range(0, z):
        print(do_x(wordz, z, delimz))


def do_x(wordx, x, delimx):
    message = ""
    for y in range(0, x):
        message = message + concat_delim(wordx, delimx)
    return message


print_z("aAa", 5, "|")
