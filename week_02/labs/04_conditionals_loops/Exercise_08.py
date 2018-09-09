'''
Demonstrate the use of the "break" statement to exit a loop.

'''
x = 1
y = 1000
while x > 0:
    print(x)
    y = y - 1
    if y == 990:
        break
    x += 1
