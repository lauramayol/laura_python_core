'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''


dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}

dict_list = (dict_1, dict_2, dict_3)
final_dict = dict()

for d in dict_list:
    for key in d:
        final_dict[key] = d[key]
print(final_dict)

for key in final_dict:
    print(key, final_dict[key])
