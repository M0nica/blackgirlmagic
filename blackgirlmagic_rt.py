import config
import time
from twython import Twython, TwythonError

# create a Twython object by passing the necessary secret passwords
twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)

# return tweets containing #BlackGirlMagic or related terms, pulls the most recent tweets


terms = [ "#BlackGirlMagic", "#MelaninPoppin", "#BlackGirlsRock", "#BlackGirlsCode", "#CarefreeBlackGirl"]
for term in terms:

    response = twitter.search(q=term + '-filter:retweets -instagram -facebook -fb', result_type="recent", count=2)

    try:
        [twitter.retweet(id = tweet["id_str"]) for tweet in response['statuses']]
    except TwythonError as e:
        print(e)
    time.sleep(15)
