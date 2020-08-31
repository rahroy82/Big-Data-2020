from kafka import KafkaProducer

bootstrap_servers = ['localhost:9099']
topicName ='myTopic'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

ack = producer.send(topicName, b'A wise man makes his own decisions.An ignorant man follows public opinions')

metadata = ack.get()
print(metadata.topic)
print(metadata.partition)
