'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''


def char_analysis(message):
    input_trimmed = (message.replace(" ", ""))
    analysis_dict = {"Upper case:": 0, "Lower case:": 0, "Punctuation:": 0, "Numbers:" : 0, "Total characters:": len(input_trimmed)}
    # Classify each character in its category.
    for a in input_trimmed:
        if a.islower():
            analysis_dict["Lower case:"] += 1
        elif a.isalpha():
            analysis_dict["Upper case:"] += 1
        elif a.isnumeric():
            analysis_dict["Numbers:"] += 1
        elif not a.isalnum():
            analysis_dict["Punctuation:"] += 1
    return analysis_dict


def print_dictionary(d):
    for i in d:
        print(i, d[i])


user_input = input()

print_dictionary(char_analysis(user_input))
