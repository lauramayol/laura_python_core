'''
Print out every prime number between 1 and 100.

'''

for check_prime in range(1, 100):
    for x in range(2, check_prime):
        if check_prime % x == 0:
            break
    else:
        print(check_prime)
