'''
Complete Exercise 3.3 (p.27) from the textbook.

'''


def right_justify(s):
    spaces = (" " * (70 - len(s)))
    message = spaces + s
    return message


print(right_justify("allen"))
