import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado: " + str(rc))

def send_mqtt_message(client, topic, msg):
   
    try:
        client.publish(topic, payload=msg, qos=1)
        print(f"Mensagem enviada: \n{msg}")
                      
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()
        print("Desconectado do broker MQTT")


def start(broker_address, port):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker_address, port, 60)
    client.loop_start()
    return client


broker_address = "mqtt.eclipseprojects.io"
port = 1883
topic = "reading/temp" 

data = [
    '{ "id": "lj01f02", "tipo": "freezer", "temperatura": -18,"timestamp": "01/03/2024 14:30"}',
    '{ "id": "lj01f41",   "tipo": "geladeira",  "temperatura": 5,   "timestamp": "01/03/2024 14:35" }',
    '{ "id": "lj01f42",   "tipo": "freezer",  "temperatura": -26,   "timestamp": "01/03/2024 14:36" }',
    '{ "id": "lj01f44",   "tipo": "geladeira",  "temperatura": 12,   "timestamp": "01/03/2024 14:38" }',
]

mqtt_client = start(broker_address, port)

try:
    for info in data:
        send_mqtt_message(mqtt_client, topic, info)
        time.sleep(3)
        
except KeyboardInterrupt:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    print("Desconectado do broker MQTT")