
from twython import Twython, TwythonError

# create a Twython object by passing the necessary secret passwords
twitter = twython.Twython(api_key, api_secret, access_token, token_secret)

# return tweets cotaining #BlackGirlMagic, mix of recent and popular tweets
response = twitter.search(q='"#BlackGirlMagic"  -filter:retweets', result_type="recent", count=100)
#if r['retweet_count'] for r in responses['statuses']> 10:
# [r['text'] for r in response['statuses'] if r['retweet_count'] > 1]
try:
    [twitter.retweet(id = tweet["id_str"]) for tweet in response['statuses'] if tweet['retweet_count'] > 1]
except TwythonError as e:
    print(e)
