import paho.mqtt.client as mqtt

MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 40
MQTT_Topic = "Home/#"

def on_connect(mosq, obj, flags, rc):
	mqttc.subscribe(MQTT_Topic, 0)

def on_message(mosq, obj, msg):
    print("MQTT data received...")
    print("MQTT Topic:" , str(msg.topic))
    print("Message:", str(msg.payload))

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

mqttc.loop_forever()
