'''
Use a one-line list comprehension to express the following functionality:

letters = []

for letter in 'suchalongword':
    letters.append(letter)

print(letters)

'''
#Below is old solution
letters = []

for letter in 'suchalongword':
    letters.append(letter)

print(letters)

#Below is new solution
letters2 = [let for let in 'suchalongword']
print(letters2)

#Check if they match!
print(letters == letters2)
