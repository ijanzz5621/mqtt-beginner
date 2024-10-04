import pika, sys, os
from pika.credentials import PlainCredentials

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host="192.168.0.101", 
        virtual_host="general_vhost", \
        credentials=PlainCredentials("general", "p@ssw0rd!")))
    
    channel = connection.channel()

    channel.queue_declare(queue='general_queue')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='general_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)