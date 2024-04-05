import paho.mqtt.client as mqtt # this library provides MQTT client functionality in Python
import random, json # this library is used for encoding and decoding JSON data
import datetime

from broker import broker # uses the global broker settings

def on_connect(client, userdata, rc): # connects the device to the broker
	if rc != 0:
		print("Unable to connect to MQTT Broker...")
	else:
		print("Connected with MQTT Broker: ") + str(broker.mqtt_broker)

def publish_To_Topic(topic, message):
	mqttc.publish(topic, message)
	print("Published: " + str(message) + " on MQTT Topic: " + str(topic))

def run_program(): # QOL improvement to check if correct settings are in use
    proceed = input(f"Proceed with the following settings: {broker.mqtt_broker}, {broker.mqtt_port}, {broker.keep_alive_interval}, Y/N? ")
    if proceed == Y:
        mqttc.connect(str(broker.mqtt_broker), int(broker.mqtt_port), int(broker.keep_alive_interval))
    elif proceed == N:
        input("Please change the settings. ")
        quit
    else:
        run_program()

def on_publish(client, userdata, mid):
	pass

def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass

MQTT_Topic_Humidity = "Home/BedRoom/Humidity"

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish

run_program()

Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(5, 90)))
Humidity_Data = {}
Humidity_Data['Type'] = "Hydrometer"
Humidity_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
Humidity_Data['Humidity'] = Humidity_Fake_Value
humidity_json_data = json.dumps(Humidity_Data)

publish_To_Topic(MQTT_Topic_Humidity, humidity_json_data)
