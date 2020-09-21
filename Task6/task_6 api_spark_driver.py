import sys

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


def handle_rdd(rdd):
    if not rdd.isEmpty():
        global ss
        df = ss.createDataFrame(rdd schema = ['key', 'value'])
        df.show(truncate=False)

# create Spark context with Spark configuration

sc = SparkContext(appName='ticker-info')
ssc = StreamingContext(sc, 5)

ss = SparkSession.builder.appName("ticker-info").getOrCreate()

ss.sparkContext.setLogLevel('WARN')

# connection to Kafka

ks = KafkaUtils.createDirectStream(ssc,['myTopic'],{'metadata.broker.list': 'localhost:9099'})


lines = ks.map(lambda x: x[])

transform = lines.map(lambda myTopic: (myTopic.split(",")))

transform.foreachRDD(handle_rdd)

ssc.start()
ssc.awaitTermination()
