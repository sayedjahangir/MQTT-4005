import paho.mqtt.client as mqtt # this library provides MQTT client functionality in python
import json # this library is used for encoding and decoding JSON data
from MQTTClient import MqttClient

from broker import broker # uses the global broker settings
from failed_connection import text_dump # dumps to a text file if there's an error

def turnLightOn(): # publishes a message to turn the light on
    client.publish("localhost/light/livingroom/set", '{"state": "ON"}')

def turnLightOff(): # publishes a message to turn light off
    client.publish("localhost/light/livingroom/set", '{"state": "OFF"}')

def onMessage(client, userdata, msg): # gets called whenever a message is recieved from the MQTT broker 
    topic = msg.topic
    payload = msg.payload.decode("utf-8")
    print(topic)
    print(payload)
    data = json.loads(payload)
    if data['occupancy']:
        print("There is a hand.")
    else:
        print("There is no hand.")

def on_connect(client, userdata, rc): # connects the device to the broker
	if rc != 0:
		print("Unable to connect to MQTT Broker...")
        # text_dump(input)
	else:
		print("Connected with MQTT Broker: ") + broker.mqtt_broker

client = MqttClient(False).client # creates an MQTT client

client.subscribe("Home/LivingRoom/Lighting") # subscribes to the topic
client.on_message = onMessage # sets the 'on_message' callback to the 'OnMessage' function defined earlier

while(True):  # it enters a infinite loop to keep the program alive
    x = 1