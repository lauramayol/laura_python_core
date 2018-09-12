'''
Complete Exercise 8.4 (p.96) from the textbook by writing out the docstrings for the functions.
 """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """

'''
def any_lowercase1(s):
    #Checks if the first character, c, of s string is lowercase and returns True, otherwise False.
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    #Checks if the string 'c' is lowercase and returns True.
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    #Checks if each character, c, of s string is lowercase and returns the boolean value according to last character.
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    #Checks if each character, c, of s string is lowercase and assigns this boolean value to flag until a lowercase value is found. Once lowercase value is found, flag will be assigned True and remain True regardless of the value for the remaining letters. The value of flag is returned once all characters in s string have been checked.
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    #Checks if each character, c, of s string is not lowercase. If any character is not lowercase (ie. uppercase), function will return False. Otherwise True.
    for c in s:
        if not c.islower():
            return False
    return True
