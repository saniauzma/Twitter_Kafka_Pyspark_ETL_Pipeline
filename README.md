# Twitter Real-time Data Pipeline

![image](https://user-images.githubusercontent.com/73434008/174433559-4d7a1026-333d-4631-baab-5b729664e775.png)

# Architecture



![Slide1](https://user-images.githubusercontent.com/73434008/174433844-e4831e1c-bf6f-4df2-a853-51a10b601951.JPG)





### Pipeline Consists of following modules:

- Twitter API V2
- Twitter Python Wrapper : Tweepy
- Apache Kafka for producing data stream
- Pyspark streaming for reading the stream data


### Overview

Data is captured in real time from the Twitter API, using the Tweepy Python wrapper (View usage - [Data Producer Module](https://github.com/saniauzma/Twitter_Kafka_Pyspark_ETL_Pipeline/blob/main/twitter_kafka_stream_producer.py)). The data collected from the Twitter API is streamed using kafka producer and published to kafka topic. Spark streaming is used to connect to the kafka server and print the real-time tweets data to the console for now.

/* ETL Flow */

## Environment Setup

#### OS Used : WSL Ubuntu 
#### Setting up Kafka :
Installed and ran confluent kafka locally on Ubuntu

You can download by running below command: 
```sh
curl -O http://packages.confluent.io/archive/7.1/confluent-community-7.1.1.tar.gz
```
To install [this](https://www.youtube.com/watch?v=mdcIdzYHFlw) YT video might be helpful.

To start all kafka services 
```sh
confluent local services start

```

For getting stream data from twitter we be using Twitter API. Go to [Twitter Developer Platform](https://developer.twitter.com/en) to create an app and save the credentials that wil be used to login to the app.


```python
#crdentials
```
In this project I have used Twitter API V2.because of filtered stream










