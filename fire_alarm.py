import paho.mqtt.client as mqtt
import json
from MQTTClient import MqttClient

# callback function for MQTT message
def on_message(client, userdata, message):
   payload = str(message.payload.decode("utf-8"))
   if payload == "fire":
       print("Fire detected! Triggering alarm.")
       alarm_triggered()

# function to trigger the alarm
def alarm_triggered():
   GPIO.output(ALARM_PIN, GPIO.HIGH)  # turn on the alarm

# function to stop the alarm
def alarm_stop():
   GPIO.output(ALARM_PIN, GPIO.LOW)  # turn off the alarm

client = MqttClient(False).client # creates an MQTT client 

client.subscribe("##/smart_lighting/new") # subscribes to the topic
client.on_message = onMessage # sets the 'on_message' callback to the 'OnMessage' function defined earlier