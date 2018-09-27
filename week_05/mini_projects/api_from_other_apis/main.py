import tweet
import wiki
from pprint import pprint

print("Enter a movie name to get its location and current top 10 Twitter trends:")
user_input = input()

my_movie = wiki.Movies(user_input)
movie_location = my_movie.get_location()

try:
    movie_coord_full = movie_location['coordinates']['value'].lower()
except:
    print("Not found. Please enter another movie name.")
else:
    # The coordinates come in this format: Point(long, lat)
    movie_format = movie_coord_full.replace('point', '').replace(')', '').replace('(', '')
    movie_coord = movie_format.split()

    my_trend = tweet.Trends()
    my_api = my_trend.set_tweep_connection()

    my_trend.get_location_trends(my_api, movie_coord[1], movie_coord[0])
