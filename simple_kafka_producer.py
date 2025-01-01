import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
producer = KafkaProducer(bootstrap_servers=['192.168.1.28:9092'])

# Enter topic name
topic_name = "topic03"

for i in range(1, 1000):
    message = 'This is message - %s' %str(i)
    future = producer.send(topic_name,  value=str.encode(message))
    try:
        record_metadata = future.get(timeout=10)
        print("message -->", message)
        print("topic -->", record_metadata.topic)
        print("partition -->", record_metadata.partition)
        print("offset -->", record_metadata.offset)
        time.sleep(0.5)
    except KafkaError as e:
        print("Error while sending message to Kafka ", e)
