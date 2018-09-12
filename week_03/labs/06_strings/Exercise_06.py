'''
Complete exercises in section 8.7 (p.75)

CODE:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

1) - Encapsulate this code in a function named count,
and generalize it so that it accepts the string and the letter as arguments.

2) - Rewrite this function so that instead of traversing the string,
it uses the three-parameter version of find from the previous section.

'''
word = 'banana'


def count(word, l):
    ct = 0
    for x in range(0, len(word)):
        if word.find(l, x) == x:
            ct += 1
    return ct


print(count(word, 'a'))
