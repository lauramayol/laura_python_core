'''
Build a simple aggregator function.

'''


def avg_function(*x):
    try:
        arg_list = [float(num) for num in x]
    except:
        print("Error with converting float.")
    else:
        arg_avg = sum(arg_list) / len(arg_list)
    return arg_avg


print(avg_function(10, 50, 100))
