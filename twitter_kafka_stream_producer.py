import json
from kafka import KafkaProducer
import tweepy
from tweepy import StreamingClient


#api_key = "yPu5p6GZ2Ioj3kwfiEVor4NcX"
#api_key_secret = "hHbrux9tTWjgqRpK1G1J0NZT3ilHfOiCposnnnZT7nKqBcISXC"
#access_token = "1533020502327185408-r1Kj7tsmONrQVYkiAsprQsAUHhn5Hc"
#access_token_secret = "cW0nDGPKzAMmzeYWCEXHcSRd2U6ckkQcgr7Yj0RLGWuDR"
access_bearer_token = "AAAAAAAAAAAAAAAAAAAAANxTdQEAAAAAXiis47XeMFxuerupH4poMSfJJas%3D1TuvkdXgUt2FjpKG7WUg99Xb1cSEBEUILh6bPuRBIQal6v1JYi"

TOPIC_NAME = 'twitter'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))


class DisplayTweet(tweepy.StreamingClient):
    def on_data(self, data):
        data_js = json.loads(data)
        data_l = data_js['data']
        producer.send(TOPIC_NAME, data_l)


DisplayTweet = DisplayTweet(access_bearer_token, wait_on_rate_limit=True)

# Add filters to track mentions
rule = tweepy.StreamRule(value="python", tag="python")
rule2 = tweepy.StreamRule(value='Dalle 2', tag='dalle2')

#Since BTS tweets are always coming, stream have many tweets to display
rule2 = tweepy.StreamRule(value='BTS', tag='BTS')
DisplayTweet.add_rules(add=[rule, rule2])

#getting the rule details
print(DisplayTweet.get_rules())

#deleting certain rule
# DisplayTweet.delete_rules(ids=['1536776873942065152','1536776873942065153'])
# print(DisplayTweet.get_rules())

# DisplayTweet.sample()

DisplayTweet.filter(tweet_fields =['id','text', 'created_at'])

#to get more data from the tweet
#DisplayTweet.filter(tweet_fields =['id','text', 'created_at'],expansions=['author_id'], user_fields= ['created_at','name','username','id','public_metrics'])