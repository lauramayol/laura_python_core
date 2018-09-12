'''
Write a script that finds the first vowel in a a user inputted string.

'''
user_input = input()
vowels = ["a", "e", "i", "o", "u"]

for letter in user_input:
    if letter in vowels:
        print(letter)
        break
