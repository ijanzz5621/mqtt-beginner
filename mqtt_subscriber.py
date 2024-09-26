import paho.mqtt.client as mqtt
import time

# callback functions
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))

mqttBroker = "localhost"
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqttBroker, port=1883)

# client.loop_start()

client.subscribe("TEMPERATURE")

# time.sleep(30)
# client.loop_stop()
client.loop_forever()


