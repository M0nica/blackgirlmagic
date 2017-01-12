import config
from twython import Twython, TwythonError

# create a Twython object by passing the necessary secret passwords
twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)

# return tweets cotaining #BlackGirlMagic, mix of recent and popular tweets
# response = twitter.search(q='"#BlackGirlMagic"  -filter:retweets', result_type="recent", count=100)
response = twitter.search(q='"#BlackGirlMagic"  -filter:retweets', result_type="recent", count=2)
#if r['retweet_count'] for r in responses['statuses']> 10:
# [r['text'] for r in response['statuses'] if r['retweet_count'] > 1]
try:
    [twitter.retweet(id = tweet["id_str"]) for tweet in response['statuses']]
    # [twitter.retweet(id = tweet["id_str"]) for tweet in response['statuses'] if tweet['retweet_count'] > 1]
except TwythonError as e:
    print(e)


response = twitter.search(q='"#MelaninPoppin"  -filter:retweets', result_type="recent", count=2)

try:
    [twitter.retweet(id = tweet["id_str"]) for tweet in response['statuses']]

except TwythonError as e:
    print(e)

    response = twitter.search(q='"CarefreeBlackGirl"  -filter:retweets', result_type="recent", count=2)

    try:
        [twitter.retweet(id = tweet["id_str"]) for tweet in response['statuses']]

    except TwythonError as e:
        print(e)
