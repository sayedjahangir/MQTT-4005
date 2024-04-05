import paho.mqtt.client as mqtt
from data_to_DB import RecieveData

from broker import broker
from rsa_encryption import decrypt

MQTT_Topic = "Home/#"

def on_connect(mosq, obj, flags, rc):
	mqttc.subscribe(MQTT_Topic, 0)

def on_message(mosq, obj, msg):
    msg.payload = decrypt(msg.payload)
    print("MQTT data received...")
    print(f"MQTT Topic: {str(msg.topic)}.")
    print(f"Message: {str(msg.payload)}.")
    RecieveData(msg.topic, msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

try:
    mqttc.connect(str(broker.mqtt_broker), int(broker.mqtt_port), int(broker.keep_alive_interval))
except:
    print("Error: invalid configuration.")

mqttc.loop_forever()
