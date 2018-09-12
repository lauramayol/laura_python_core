'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

Train using string methods and loops on an open-end mini-project!

- use one block of text as verse input (hint: linebreaks can be helpful!)
- use a for loop for creating the full lyrics

'''
body = """You wake up, flawless
Post up, flawless
Ride round in it, flawless"""

lines = body.split('\n')

chorus = "I woke up like this"

for words in lines:
    print(words)
    print(chorus)
    print(chorus)
    print(chorus)
