import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

# callback functions
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttBroker = "192.168.1.101"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Temperature_Inside")

client.tls_set()
# client.username_pw_set(username="general", password="p@ssw0rd!")

client.on_connect = on_connect
# client.on_message = on_message

client.connect(mqttBroker, port=1883, keepalive=60)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic Temperature")
    time.sleep(5)

# client.loop_forever()





