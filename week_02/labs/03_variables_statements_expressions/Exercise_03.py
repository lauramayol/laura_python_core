'''
Print pi to the console using the following formula:
note that this is not the complete series to compute the true number pi.

    4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11))

'''
# I am a bit confused what the purpose is here as the value does not equal 3.14
import math
#eval_pi = 4.0 * (1 - (1.0 / 3) + (1.0 / 5) - (1.0 / 7) + (1.0 / 9) - (1.0 / 11))


operator = 0
pre_eval_pi = 1

for check_prime in range(3, 50):
    for x in range(2, check_prime):
        if check_prime % x == 0:
            break
    else:
        if operator == 0:
            pre_eval_pi = pre_eval_pi - (1.0 / check_prime)
            operator = 1
            print(check_prime)
        else:
            pre_eval_pi = pre_eval_pi + (1.0 / check_prime)
            operator = 0
            print(check_prime)
eval_pi = 4.0 * pre_eval_pi

print(eval_pi)
print(math.pi)
