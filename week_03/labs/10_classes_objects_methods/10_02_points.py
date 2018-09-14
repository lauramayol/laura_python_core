'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

The provided code to start is in file Point1.py in this folder.

'''

import Point1
import math


def distance_between_points(p1, p2):
    horiz_dist = p2.x - p1.x
    vert_dist = p2.y - p1.y
    distance = round(math.hypot(horiz_dist, vert_dist), 1)
    print(distance)


my_point = Point1.Point()
my_point.x = 3.0
my_point.y = 4.0

your_point = Point1.Point()
your_point.x = 10.0
your_point.y = 10.0

Point1.print_point(my_point)
Point1.print_point(your_point)
distance_between_points(my_point, your_point)
