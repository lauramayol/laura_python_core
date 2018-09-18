# Files

Read through chapter ["Case Study: Word Play"](http://greenteapress.com/thinkpython2/html/thinkpython2010.html) as well as chapter ["Files"](http://greenteapress.com/thinkpython2/html/thinkpython2015.html) from
Allen B. Downey's Think Python 2e book.

- How do you open a file in read mode and print the first line?
    with open("words.txt", "r") as f:
        data = f.readline()

- How can you use a for loop to iterate through the words of a file?
    with open("words.txt", "r") as fin:
    for line in fin:
        for word in line.split():
            print(word)

- What does it mean when a program is persistent?
    They run for a long time (or always) and they keep their data in permanent storage.

- How do you open a file in write mode?
    with open("output.txt", "w") as f:
        f.write("hello")

- Practice using f-strings as a replacement for the .format() method

with open("words.txt", "r") as f:
    data = f.readlines()

# print(data)

last = data[-1].rstrip()

with open("output.txt", "w") as f:
    f.write(f"Here is the last line: {last}")


- What is the difference between a relative path and an absolute path?
    relative path relates to current directory whereas absolute will point to the same place regardless of your current directory.

- What are some IOExceptions that you might encounter? How are they generated?
    Some exapmles, if you try to open() a file that doesn't exist, or if you try to readwrite a file that you do not have write access to.

- What is a try statement used for?
    To try the action you were planning to do, and if there is an error or exception, you can use an "except" clause similar to "else".

- What is an except statement used for?
    It allows you to catch an error and either try to fix it or end the program with an informative message to the user.

- Can you have a try without an except? Can you have an except without a try?
    no for both

- What is the variable `__name__` used for?
    It is set when the program runs and equals to __main__ when it is being run as a script, but not when the module is imported.
