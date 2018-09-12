'''
Complete Exercise 8.3 (p.95) from the textbook.

'''


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
