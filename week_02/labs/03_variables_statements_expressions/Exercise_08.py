'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''

#Note: the below code did not work in Sublime but it worked in Python interpreter. I tried installing SublimeREPL as per some web forums but it looks like this doesn't work for Python3.
C = float(input())
F = C * 1.8 + 32

message = str(C) + " degrees celsius = " + str(F) + " degrees farenheit"

print(message)
