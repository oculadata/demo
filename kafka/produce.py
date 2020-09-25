from kafka import KafkaProducer

def produce(topic, server, msg):
    producer = KafkaProducer(value_serializer=lambda v: v.encode('utf-8'),bootstrap_servers=[server])
    producer.send(topic, msg)

def main():
    produce('mytopic', '13.59.244.115:9092', 'abcdef')

if __name__ == '__main__':
    main()
