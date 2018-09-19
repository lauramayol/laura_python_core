'''
User python's built-in .enumerate() function to print the classes
together with their numbers from 1-4.


NOTE: a less readable, but common structure in other languages would be:

for i in range(len(courses)):
    print(f"{i}: {courses[i]} python")

'''
courses = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

for index, value in enumerate(courses, start=1):
    print(f"Level {index}: {value} python")
