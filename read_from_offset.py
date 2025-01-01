from kafka import TopicPartition
from kafka import KafkaConsumer

# Enter the values of topic, partition & offset
topic_name = 'topic03'
partition_number = 1
offset_value = 10

consumer = KafkaConsumer(bootstrap_servers=['192.168.1.28:9092'],group_id='my-consumer-group')
tp = TopicPartition(topic=topic_name, partition=partition_number)
consumer.assign([tp])
consumer.seek(tp, offset_value)

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s, type=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value.decode('utf-8'), type(message.value)))

