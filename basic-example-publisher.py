import pika
from pika.credentials import PlainCredentials
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="192.168.0.101", 
    virtual_host="general_vhost", \
    credentials=PlainCredentials("general", "p@ssw0rd!")))

channel = connection.channel()

channel.queue_declare(queue="general_queue")

while (True):
    try:
        channel.basic_publish(
            exchange='',
            routing_key='',
            body='Hello from General User'
        )
    except Exception as ex:
        print(ex)

    print('Message has been sent!')
    
    time.sleep(2)

connection.close()

