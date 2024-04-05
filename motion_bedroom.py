import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

from broker import broker # uses the global broker settings
from failed_connection import text_dump # dumps to a text file if there's an error
from rsa_encryption import encrypt # encrypts publications

def on_connect(client, userdata, rc):
	if rc != 0:
		print("Unable to connect to MQTT Broker...")
        # text_dump(input)
	else:
		print("Connected with MQTT Broker: ") + str(broker.mqtt_broker)
		
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print("")

def run_program(): # QOL improvement to check if correct settings are in use
    proceed = input(f"Proceed with the following settings: {broker.mqtt_broker}, {broker.mqtt_port}, {broker.keep_alive_interval}, Y/N? ")
    if proceed == Y:
        mqttc.connect(str(broker.mqtt_broker), int(broker.mqtt_port), int(broker.keep_alive_interval))
    elif proceed == N:
        input("Please change the settings. ")
        quit
    else:
        run_program() # asks again if user types an unexpected argument

def on_publish(client, userdata, mid):
	pass

def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass
	
MQTT_Topic_Motion = "Home/BedRoom/Motion"

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish

try:
    run_program()
except:
    print("Error: invalid configuration.")

MotionFakeData = random.choice([True, False])
MotionData = {}
MotionData['Sensor_ID'] = "PIRSensor"
MotionData['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
MotionData['Motion'] = MotionFakeData
MotionJsonData = json.dumps(MotionData)

publish_To_Topic(encrypt(MQTT_Topic_Motion), encrypt(MotionJsonData)) # calls publish function above
