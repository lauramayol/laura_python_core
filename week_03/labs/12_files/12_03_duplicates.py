'''
In a large collection of MP3 files, there may be more than one copy of
the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a
given suffix (like .mp3). Hint: os.path provides several useful
functions for manipulating file and path names.
To recognize duplicates, you can use md5sum to compute a “checksum” for
each file. If two files have the same checksum, they probably have the
same contents. To double-check, you can use the Unix command diff.
Solution: http://thinkpython2.com/code/find_duplicates.py.

Go and tackle your duplicate files! :)

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
import os

file_paths = list()


def walk(dirname, ext):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            if ext in path:
                file_paths.append(path)
        else:
            walk(path, ext)
    return file_paths


def file_md5(f1):
    cmd = "md5 -r " + f1
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    return res.replace(f1, "")


def check_files(f1, f2):
    return file_md5(f1) == file_md5(f2)


file_list = walk("/Users/lauramay/Documents/CodingNomads", ".txt")
matched_list = list()
x = 1
for x in range(1, len(file_list)):
    if check_files(file_list[x], file_list[x - 1]):
        matched_list.append(file_list[x - 1])
        matched_list.append(file_list[x])

print(matched_list)
