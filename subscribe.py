import paho.mqtt.client as mqtt
from data_to_DB import RecieveData

MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 40
MQTT_Topic = "Home/#"

def on_connect(mosq, obj, flags, rc):
	mqttc.subscribe(MQTT_Topic, 0)

def on_message(mosq, obj, msg):
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

mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

mqttc.loop_forever()
