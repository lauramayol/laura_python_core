'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''


def sed(find_string, replace_with, f1, f2):
    try:
        with open(f1, "r") as f:
            data = f.readlines()
    except:
        print(f"Cannot read file {f1}")
    else:
        new_data = ""
        for word in data:
            new_data += word.replace(find_string, replace_with)
        write_file(new_data, f2)


def write_file(message, fwrite):
    try:
        with open(fwrite, "w") as f:
            f.write(message)
    except:
        print(error)


sed("e", "!!", "words.txt", "output.txt")
