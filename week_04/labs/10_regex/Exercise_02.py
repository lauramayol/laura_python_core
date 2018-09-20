'''
Do RegExExercises on https://www.w3resource.com/python-exercises/re/

Complete:
  * 20 Exercises for a bronze badge
 ** 35 Exercises for a silver badge
*** 50 Exercises for a golden badge

P.S.: I don't actually have real metal badges, but if you do the work
I'll draw you a badge in Paintbrush or on paper ;)

'''
import re
my_string = "Whoa9_zbbbabyZ"
# 1
#my_string = "HereismyTESTstring0"


def only_numchars(msg):
    check_regex = re.search(r"^[A-Z|a-z|0-9]+$", msg)
    ans = bool(check_regex)
    print(check_regex)
    print(ans)


only_numchars(my_string)

# 2


def a_to_bs(msg):
    if re.search(r"ab*?", msg):
        print("Found a match with ab*?")
    else:
        print("Did not match ab*?")


a_to_bs(my_string)

# 3


def a_to_bs2(msg):
    if re.search(r"ab+", msg):
        print("Found a match with ab+")
    else:
        print("Did not match ab+")


a_to_bs2(my_string)

# 4


def a_to_bs3(msg):
    if re.search(r"ab?", msg):
        print("Found a match with ab?")
    else:
        print("Did not match ab?")


a_to_bs3(my_string)

# 5


def a_to_bs4(msg):
    if re.search(r"ab{3}", msg):
        print("Found a match with ab3")
    else:
        print("Did not match ab3")


a_to_bs4(my_string)

# 6


def a_to_bs5(msg):
    if re.search(r"ab{2,3}", msg):
        print("Found a match with ab2-3")
    else:
        print("Did not match ab2-3")


a_to_bs5(my_string)

# 7


def lc_with_underscore(msg):
    if re.search(r"^[a-z]+_[a-z]+$", msg):
        print("Found a match with a_z")
    else:
        print("Did not match a_z")


lc_with_underscore(my_string)
# 8


def upper_with_lc(msg):
    if re.search(r"^[A-Z][a-z]+$", msg):
        print("Found a match with Az+")
    else:
        print("Did not match Az+")


upper_with_lc(my_string)

# 9


def start_a_end_b(msg):
    if re.search(r"^a.*b$", msg):
        print("Found a match with a.b")
    else:
        print("Did not match a.b")


start_a_end_b(my_string)

# 10


def match_start_word(msg, word):
    if re.search(rf"^{word}.*", msg):
        print(f"Found a match with start {word}")
    else:
        print(f"Did not match start {word}")


match_start_word(my_string, "baby")

# 11


def match_end_word(msg, word):
    if re.search(rf".*{word}[!?.]*$", msg):
        print(f"Found a match with ending '{word}'")
    else:
        print(f"Did not match ending '{word}'")


match_end_word(my_string, "baby")

# 12


def match_letter(msg, letter):
    if re.search(rf"{letter}+", msg):
        print(f"Found a match with '{letter}'")
    else:
        print(f"Did not match '{letter}'")


match_letter(my_string, "z")

# 13


def mid_letter(msg, letter):
    if re.search(rf"\B{letter}\B", msg):
        print(f"Found a match with '{letter}'")
    else:
        print(f"Did not match '{letter}'")


mid_letter(my_string, "z")
# 14 Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


def only_alpha_num(msg):
    if re.search(rf"^\w+$", msg):
        print(f"Found a match with only letters, nums, _")
    else:
        print(f"Did not match only letters, nums, _")


only_alpha_num(my_string)

# 15 Write a Python program where a string will start with a specific number.


def start_w_num(msg, num):
    if re.search(rf"^{num}", msg):
        print(f"Found a match with starting {num}")
    else:
        print(f"Did not match starting {num}")


start_w_num(my_string, 9)

# 16 Write a Python program to remove leading zeros from an IP address.
ip_address = "216.08.094.196"


def remove_lead_char(msg, num):
    new_msg = re.sub(rf"^{num}*", "", msg)
    print(re.sub(rf"\.{num}", ".", new_msg))
    #     print(f"Found a match with starting {num}")
    # else:
    #     print(f"Did not match starting {num}")


remove_lead_char(ip_address, 0)

# 17 17. Write a Python program to check for a number at the end of a string.


def end_w_num(msg):
    if re.search(rf"[0-9]$", msg):
        print(f"Found a match with ending num")
    else:
        print(f"Did not match ending num")


end_w_num(my_string)

# 18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.


def has_num(msg):
    if re.search(r"[0-9]{1,3}", msg):
        print(f"Found a match with num*1-3")
    else:
        print(f"Did not match num*1-3")


has_num(my_string)

# 19. Write a Python program to search some literals strings in a string.
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']
d = {}
for word in searched_words:
    d[word] = bool(re.search(word, sample_text))
print(f"Words found in text {d}")

# 20. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.

d = {}
for word in searched_words:
    check = re.search(word, sample_text)
    if check:
        d[word] = check.span()[0]
print(f"Words found in text {d}")
