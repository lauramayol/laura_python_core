'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

fint = "integers.txt"

try:
    fint = open(fint)
    data = fint.readlines()
except:
    print(f"Cannot read file {fint}")
else:
    prior_num = 0
    for num in data:
        try:
            num_int = int(num)
            pct_dif = (num_int - prior_num) / prior_num
            print(f"The % difference between {num_int} and {prior_num} is: {round(pct_dif * 100, 0)}%")
        except ValueError:
            print(f"Could not convert {num} to an integer.")
        except ZeroDivisionError:
            print(f"{num_int} skipped because of zero division error with prior number.")
            pass
        except:
            print("Unknown error occurred")
            break
        finally:
            prior_num = num_int
