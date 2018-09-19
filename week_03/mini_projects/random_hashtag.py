'''
--------------------------------------------------------
                RANDOM HASHTAG GENERATOR
--------------------------------------------------------

Programmatically generate random hashtags by picking from a word list.

Tip: In UNIX systems you can access a dictionary file at this path:
        /usr/share/dict/words

'''
import random


def create_list(path):
    fin = open(path)
    word_list = []
    for line in fin:
        word_list.append(line.strip())
    return word_list


def pick_random(t):
    random_word = random.choice(t)
    return random_word


word_list = create_list('/usr/share/dict/words')

print("Enter a word to use in your custom hashtag, or press Enter for random generated:")
pick_a_word = input()
paired = pick_random(word_list)

if pick_a_word == "":
    pick_a_word = pick_random(word_list)

print(f"Your custom hashtag is: #{pick_a_word}{paired}")
