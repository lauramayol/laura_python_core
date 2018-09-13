'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple
Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.
'''


def sorted_list(nums):
    nums.sort()
    if len(nums) % 2 > 0:
        nums.append(0)
    first_list = list()
    second_list = list()
    for x in range(0, len(nums)):
        if x % 2 == 0:
            first_list.append(nums[x])
        else:
            second_list.append(nums[x])
    combined = zip(first_list, second_list)

    for pair in combined:
        print(pair)

    return combined


t = [11, 13, 5, 1, 3]
print(sorted_list(t))
