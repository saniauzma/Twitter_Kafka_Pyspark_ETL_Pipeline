#command to run this file: spark-submit spark_tw.py
#spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 spark_tw.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *



# init spark here
import time

kafka_topic_name = "twitter"
kafka_bootstrap_servers = 'localhost:9092'

if __name__ == "__main__":
    print("welcome to spark!\n stream Data processing Application started...")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    
    spark = SparkSession.builder.appName("Tweeter").master("local[4]").getOrCreate()
    
    
    spark.sparkContext.setLogLevel("ERROR")
    
    twitter_stream_df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", kafka_bootstrap_servers)\
        .option("subscribe", kafka_topic_name).option("startingOffsets", "latest")\
        .option("max.poll.records", 100) \
        .option("failOnDataLoss", False) \
        .load()
    
    
    print("printing schema of twitter df")
    
    twitter_stream_df.printSchema()

    # twitter_schema = StructType([\
    #                     StructField("data",\
    #                         StructType([\
    #                             StructField("author_id",StringType(), False),\
    #                             StructField("created_at",StringType(), False),\
    #                             StructField("id",StringType(), False),\
    #                             StructField("text",StringType(), False)])\
    #                         , False)\
    #                     ,StructField("matching_rules",\
    #                         ArrayType(\
    #                             StructType([\
    #                                 StructField("id", StringType(), False),\
    #                                 StructField("tag", StringType(), False) ])
    #                             , False)
    #                         , False)]
    #                 )

    twitter_schema = StructType([
        StructField("created_at", StringType(), False),
        StructField("id",         StringType(), False),
        StructField("text",       StringType(), False)])



    
    twitter_records = twitter_stream_df.selectExpr("CAST(key AS STRING)", "CAST(value as STRING) as twitter_data")\
        .select(from_json("twitter_data", schema=twitter_schema).alias("twitter_data"))
    
    # tw_flat = twitter_records.select("twitter_data")\
    #     .select("twitter_data.data.author_id", "twitter_data.data.created_at", "twitter_data.data.id", "twitter_data.data.text", explode("twitter_data.matching_rules").alias("m_rule"))\
    #     .select("author_id", "created_at", "id", "text", "m_rule.id", "m_rule.tag")

    tweeter_data = twitter_records.select("twitter_data")\
        .select("twitter_data.*")


        
    tweeter_data.printSchema()

    #here more data processing or transformation can be done
    #but for now we are just printing the data
    


    tweeter_stream = tweeter_data.writeStream.format("console").outputMode("append").start()
    tweeter_stream.awaitTermination()
    print("stream Data processing Application finished...")

    