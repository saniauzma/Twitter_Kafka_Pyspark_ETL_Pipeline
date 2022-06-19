# Twitter Real-time Data Pipeline

![image](https://user-images.githubusercontent.com/73434008/174433559-4d7a1026-333d-4631-baab-5b729664e775.png)

## Architecture



![Slide1](https://user-images.githubusercontent.com/73434008/174433844-e4831e1c-bf6f-4df2-a853-51a10b601951.JPG)





### Pipeline Consists of following modules:

- Twitter API V2
- Twitter Python Wrapper : Tweepy
- Apache Kafka for producing data stream
- Pyspark streaming for reading the stream data


## Overview

Data is captured in real time from the Twitter API, using the Tweepy Python wrapper (View usage - [Data Producer Module](https://github.com/saniauzma/Twitter_Kafka_Pyspark_ETL_Pipeline/blob/main/twitter_kafka_stream_producer.py)). The data collected from the Twitter API is streamed using kafka producer and published to kafka topic. Spark streaming is used to connect to the kafka server and print the real-time tweets data to the console for now.

<!-- ### ETL Flow -->

## Environment Setup

#### OS Used : WSL Ubuntu 
#### Python : Python 3.7.1
#### Setting up Kafka :
- Installed and ran [confluent kafka](https://www.confluent.io/) locally on Ubuntu.

We can download by running below command: 
```sh
curl -O http://packages.confluent.io/archive/7.1/confluent-community-7.1.1.tar.gz
```
To install [this](https://www.youtube.com/watch?v=mdcIdzYHFlw) YT video might be helpful.

- To start all kafka services run : 
```sh
confluent local services start

```
following services will be up and running.
```sh
ZooKeeper is [UP]
Kafka is [UP]
Schema Registry is [UP]
Kafka REST is [UP]
Connect is [UP]
ksqlDB Server is [UP]
Control Center is [UP]
```
- Go to localhost:9021 and create a topic named "twitter" in the confluent kafka cluster.

- To verify if kafka is working fine, we can run producer and consumer in separate terminals and produce and consume data.

Producer command : 
```sh
kafka-console-producer --topic twitter --broker-list localhost:9092
```
Consumer command : 
```sh
kafka-console-consumer --topic twitter --bootstrap-server localhost:9092 --from-beginning
```



### Creating Twitter App

[Twitter API Docs](https://developer.twitter.com/en/docs)

- For getting stream data from twitter I have used Twitter API. Go to [Twitter Developer Platform](https://developer.twitter.com/en) to create an app and save the credentials that will be used to login to the app.


```python
#credentials

api_key = ""         #aka consumer_key
api_ket_secret = ""  #aka consumer_key_secret
bearer_token = ""
access_token = ""
access_token_secret = ""
```
- In this project I have used Twitter API V2, because it has the filtered stream endpoint that lets you filter real time stream of public tweets by applying a set of rules.
For Example: 

rule 1 - search for value "python" and tag "python".

- How does an API response look?

[This Twitter API v2 data dictionary ](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) from API's Docs illustrates the structure for the tweet object.

In this project I have filtered ‘root-level’ fields, such as ```id, text, and created_at```

- More fields like [user fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user), [media fields](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media), etc. can be filtered.

- To learn more about filtered stream please refer Twitter API's [official Docs](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction).
### Setting up a virtual environment 
- Install python3-venv : 
```sh
sudo apt install python3-venv
```
- Create a virtual environment : 
```sh
python3 -m venv env
```
- Activate env :
```sh
source env/bin/activate
```

### Installing required Python libraries 
In this project, mainly three Python libraries are used.
- tweepy 
- kafka-python
- pyspark (make sure it's version compatible with python's version)

Install using requirement.txt : 
```sh
pip install -r requirements.txt
```

### Tweepy

[tweepy Doc](https://docs.tweepy.org/en/stable/index.html)

- Installing using pip ``` pip install tweepy ```
- Tweepy has Twitter API v2 reference. We can connect using [```tweepy.StreamingClient```](https://docs.tweepy.org/en/stable/streamingclient.html) to filter and sample realtime Tweets.
- Usage - [twitter_kafka_stream_producer Module](https://github.com/saniauzma/Twitter_Kafka_Pyspark_ETL_Pipeline/blob/main/twitter_kafka_stream_producer.py)

### kafka-python

[kafka-python Docs](https://kafka-python.readthedocs.io/en/master/#)
- Installing using pip ``` pip install kafka-python ```
- Used kafka-python to produce tweets data stream to the kafka topic.
- Usage - [twitter_kafka_stream_producer Module](https://github.com/saniauzma/Twitter_Kafka_Pyspark_ETL_Pipeline/blob/main/twitter_kafka_stream_producer.py)


### pyspark

[pyspark-3.2.1 Docs](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)

- Installing using pip ``` pip install pyspark ```
- To read the stream from the kafka producer spark structured streaming is used.
- Here's the schema of the final output to the console : 
```python
 twitter_schema = StructType([
        StructField("created_at", StringType(), False),
        StructField("id",         StringType(), False),
        StructField("text",       StringType(), False)])
        
```
- Usage - [twitter_pyspark_streaming Module](https://github.com/saniauzma/Twitter_Kafka_Pyspark_ETL_Pipeline/blob/main/twitter_pyspark_streaming.py)
- Submit the spark job using below command : 
```sh
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 twitter_pyspark_streaming.py
```

## Demonstration of the twitter data stream, by running the modules in separate terminals : 

<iframe width="560" height="315" src="https://www.youtube.com/embed/T0TW_gF-O3c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



















