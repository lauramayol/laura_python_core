'''
Use the external python module 'markovify' to create short text snippets
of your favorite text resource.

https://github.com/jsvine/markovify

CHALLENGE: rewrite it using `markovbot` to let the bot tweet
some wisdom once in a while!
https://github.com/esdalmaijer/markovbot

'''
import markovify

# Get raw text as string.
with open("trump_state_of_union_2018.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(3):
    print(text_model.make_short_sentence(140))
