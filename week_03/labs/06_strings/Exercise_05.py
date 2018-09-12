'''
Write a script that takes a user inputed string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''
user_input = input()
print("All letters capitalized: " + user_input.upper())
print("All letters lower case: " + user_input.lower())


vowels = ["a", "e", "i", "o", "u"]
result = ""
for letter in user_input:
    if letter.lower() in vowels:
        result = result + letter.lower()
    else:
        result = result + letter.upper()
print("All vowels lower and consonants upper: " + result)
