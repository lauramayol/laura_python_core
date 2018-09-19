'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

# remember: range() also creates a generator object (try printing it!)
nums = range(1, 1000000)


def check_divisible(r, d):
    nums_gen = (n for n in r if n % d == 0)
    for n in nums_gen:
        print(n)


check_divisible(nums, 1111)
