'''
Using the tweepy package, build a script that classifies a twitter handle
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''
import tweepy
import os

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET_KEY"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_group = {"Over 1M": list(), "500K to 1M": list(), "50K to 500K": list(), "less than 50K": list()}
print("We are searching people in Twitter. Please enter what topic you would like to search:")
user_input = input()
ct = 0
for u in tweepy.Cursor(api.search_users, q=(user_input)).items(500):
    user_tuple = (u.screen_name, u.followers_count)
    ct += 1
    if user_tuple not in user_group:
        if u.followers_count > 1000000:
            user_group["Over 1M"].append(user_tuple)
        elif u.followers_count >= 500000:
            user_group["500K to 1M"].append(user_tuple)
        elif u.followers_count >= 50000:
            user_group["50K to 500K"].append(user_tuple)
        else:
            # elif u.followers_count > 0:
            user_group["less than 50K"].append(user_tuple)

print(f"Twitter handle | # Followers (Top {ct} records)")
for key in user_group:
    print(f"{key} followers: ")
    for u in sorted(user_group[key], key=lambda tup: tup[1], reverse=True):
        print(f"@{u[0]} | {u[1]}")


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# Get the User object for twitter...
# user = api.get_user('twitter')

# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)

# for tweet in tweepy.Cursor(api.search, q=('yoga')).items(5):
#     print("Screen-name:", tweet.author.screen_name.encode('utf8'))
#     print("Tweet created:", tweet.created_at)
#     print("Tweet:", tweet.text.encode('utf8'))
#     # print "Retweeted:", tweet.retweeted
#     # print "Favourited:", tweet.favorited
#     print("Location:", tweet.user.location.encode('utf8'))
#     # print "Time-zone:", tweet.user.time_zone
#     # print "Geo:", tweet.geo
#     print(tweet.entities.get('hashtags'))
#     print("//////////////////")
