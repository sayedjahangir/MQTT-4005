import paho.mqtt.client as mqtt # this library provides MQTT client functionality in Python
import random, json # this library is used for encoding and decoding JSON data
import datetime

from broker import broker # uses the global broker settings
from failed_connection import text_dump # dumps to a text file if there's an error
from rsa_encryption import encrypt # encrypts publications

def on_connect(client, userdata, rc): # connects the device to the broker
	if rc != 0:
		print("Unable to connect to MQTT Broker...")
        # text_dump(input)
	else:
		print("Connected with MQTT Broker: ") + str(broker.mqtt_broker)

def publish_To_Topic(topic, message):
	mqttc.publish(topic, message)
	print(f"Published: {str(message)} on MQTT Topic: {str(topic)}.")

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

MQTT_Topic_Humidity = "Home/LivingRoom/Humidity"

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish

try:
    run_program()
except:
    print("Error: invalid configuration.")

Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(50, 100)))
Humidity_Data = {}
Humidity_Data['Type'] = "Hydrometer"
Humidity_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
Humidity_Data['Humidity'] = Humidity_Fake_Value
humidity_json_data = json.dumps(Humidity_Data)

publish_To_Topic(encrypt(MQTT_Topic_Humidity), encrypt(humidity_json_data))