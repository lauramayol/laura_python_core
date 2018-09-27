import tweepy
import os
from pprint import pprint


class Trends():

    def set_tweep_connection(self):
        consumer_key = os.environ["TWITTER_API_KEY"]
        consumer_secret = os.environ["TWITTER_API_SECRET_KEY"]
        access_token = os.environ["TWITTER_ACCESS_TOKEN"]
        access_token_secret = os.environ["TWITTER_ACCESS_SECRET"]

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        return api

    def get_location_trends(self, api, lat, long):

        closest_locations = api.trends_closest(lat, long)

        # Get the first closest location in Twitter based on lat, long
        for i in range(1):
            twitter_location = closest_locations[i]

        if twitter_location['placeType']['name'] == 'Country':
            print(f"Twitter found the nearest location in {twitter_location['country']}.")
        else:
            print(f"Twitter found the nearest location in {twitter_location['name']}, {twitter_location['country']}.")

        top_trends = api.trends_place(twitter_location['woeid'])[0]['trends']
        top_trends = sorted(top_trends, key=lambda dict: dict['tweet_volume'] or 0, reverse=True)

        t = top_trends[:10]
        top10 = tuple()
        for i, val in enumerate(t, start=1):
            top10 = i, val

        print("Below are your top 10 trends in Twitter:")
        pprint(top10)

# location_list = api.trends_available()
# trend_dict = {}
# trend_location = {}
# high = 0


# t = top_trends[0]
# # for t in top10_in_location[0]:
# if (t['tweet_volume'] or 0) > high:
#     high = t['tweet_volume']
#     trend_dict = t
#     #trend_location = i
# pprint(t)
# pprint(top_trends)

# for i in location_list:
#     woeid = i['woeid']
#     if woeid > 1:
#         top10_in_location = api.trends_place(woeid)[0]['trends']
#         top10_in_location = sorted(top10_in_location, key=lambda dict: dict['tweet_volume'] or 0, reverse=True)
#         t = top10_in_location[0]
#         #for t in top10_in_location[0]:
#         if (t['tweet_volume'] or 0) > high:
#             high = t['tweet_volume']
#             trend_dict = t
#             trend_location = i
# pprint(trend_dict)
# pprint(trend_location)
#trend_dict[i['woeid']] = api.trends_place(i['woeid'])

# print(api.trends_available)

# print(api.trends_place(23424925))

# user_group = {"Over 1M": list(), "500K to 1M": list(), "50K to 500K": list(), "less than 50K": list()}
# print("We are searching people in Twitter. Please enter what topic you would like to search:")
# user_input = input()
# ct = 0
# for u in tweepy.Cursor(api.search_users, q=(user_input)).items(500):
#     user_tuple = (u.screen_name, u.followers_count, u.location.encode('utf8'))
#     ct += 1
#     if user_tuple not in user_group:
#         if u.followers_count > 1000000:
#             user_group["Over 1M"].append(user_tuple)
#         elif u.followers_count >= 500000:
#             user_group["500K to 1M"].append(user_tuple)
#         elif u.followers_count >= 50000:
#             user_group["50K to 500K"].append(user_tuple)
#         else:
#             # elif u.followers_count > 0:
#             user_group["less than 50K"].append(user_tuple)
