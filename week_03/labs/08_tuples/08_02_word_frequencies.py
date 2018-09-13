'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at:
http://en.wikipedia.org/wiki/Letter_frequencies.
Solution: http://thinkpython2.com/code/most_frequent.py.

Source: Chapter on "Tuples" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2013.html

'''


def most_frequent(message):
    formatted_message = message.lower()
    num_list = list()
    letter_list = list()
    for letter in formatted_message:
        if letter not in letter_list:
            num_list.append(formatted_message.count(letter))
            letter_list.append(letter)
            #print(num_list, letter_list)
    combined = list(zip(num_list, letter_list))
    combined.sort(reverse=True)
    for num, let in combined:
        print(num, let)
    return combined


my_message = "Hello my name is Laura and I am practicing Python"
most_frequent(my_message)
