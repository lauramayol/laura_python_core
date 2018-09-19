'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
nums = range(1, 1000000)


def check_divisible(r, d):
    nums_gen = (n for n in r if n % d == 0)
    for n in nums_gen:
        print(n // d)


check_divisible(nums, 1111)
