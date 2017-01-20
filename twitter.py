import tweepy

api_key = "pg3j5HNe0C3wsiFhv027ZyOof"
api_secret = "OoNGQYDr0t6oBBId5PuQ1pA3bXsWtAAzG6LFFbTOuMMBG79DBh"
access_token = "819043902804008960-6a2UAn1TaEEiHczmb8yKcaBET8cMwkw"
access_secret = "tANtneGKb8Ud7OWYH5G5T2FTt0Qd92o3WjUGJuzIa3BK4"
owner_id = "819043902804008960"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
client = tweepy.API(auth)

client.update_status("19k og and I still missed smh fking waking up late")
