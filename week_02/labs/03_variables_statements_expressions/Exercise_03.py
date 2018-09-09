'''
Print pi to the console using the following formula:
note that this is not the complete series to compute the true number pi.

    4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11))

'''
# I am a bit confused what the purpose is here as the value does not equal 3.14
import math
eval_pi = 4.0 * (1 - (1.0 / 3) + (1.0 / 5) - (1.0 / 7) + (1.0 / 9) - (1.0 / 11))
print(eval_pi)
print(math.pi)
