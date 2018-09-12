'''
--------------------------------------------------------
                99 BOTTLES OF BEER LYRICS
--------------------------------------------------------

https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

-- GOAL --
Create a program that prints out every line to the song
"99 bottles of beer on the wall." This should be a pretty simple program,
so to make it a bit harder, here are some rules to follow.

-- RULES --
1) If you are going to use a list for all of the numbers,
    do not manually type them all in. Instead, use a built in function.
2) Besides the phrase "take one down," you may not type in any
    numbers/names of numbers directly into your song lyrics.
3) Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
4) Put a blank line between each verse of the song.

'''


def bottles(n):
    if n > 1:
        lyric = str(n) + " bottles"
    elif n == 1:
        lyric = str(n) + " bottle"
    else:
        lyric = "no more bottles"
    lyric = lyric + " of beer"
    return lyric


def bottles_on_wall(n):
    lyric2 = bottles(n) + " on the wall"
    return lyric2


nums = 99
x = nums


while x >= 0:
    print(bottles_on_wall(x).capitalize() + ", " + bottles(x) + ".")
    x = x - 1
    if x < 0:
        last_line = "Go to the store and buy some more, " + bottles_on_wall(nums)
    else:
        last_line = "Take one down and pass it around, " + bottles_on_wall(x)
    print(last_line + ".")
    print("")
