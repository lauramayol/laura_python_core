'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''
num_list = list()
num_sum = 0

for x in range(0, 10):
    num = int(input())
    num_list.append(num)
    num_sum += num
avg = num_sum / len(num_list)

print(num_list)
print("The sum is: " + str(num_sum))
print("The average is: " + str(avg))
