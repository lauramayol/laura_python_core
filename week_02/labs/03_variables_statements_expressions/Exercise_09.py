'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

#Note: the below code did not work in Sublime but it worked in Python interpreter. I tried installing SublimeREPL as per some web forums but it looks like this doesn't work for Python3.
mi = int(input())
mpg = int(input())
ppg = float(input())

cost = (mi / mpg) * ppg
print(cost)
