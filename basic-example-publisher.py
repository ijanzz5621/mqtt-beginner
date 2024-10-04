import pika
from pika.credentials import PlainCredentials

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="192.168.0.101", 
    virtual_host="general_vhost", \
    credentials=PlainCredentials("general", "p@ssw0rd!")))

channel = connection.channel()

channel.queue_declare(queue="general_queue")

channel.basic_publish(
    exchange='',
    routing_key='general_key',
    body='Hello from General User'
)

print('Message has been sent!')

connection.close()

