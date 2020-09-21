from kafka import KafkaConsumer
import sys

bootstrap_servers = ['localhost:9099']
topicName = 'myTopic'

servers = bootstrap_servers, auto_offset_reset = 'earliest')
consumer = KafkaConsumer ('topicName')
for message in consumer:
    print (message)

