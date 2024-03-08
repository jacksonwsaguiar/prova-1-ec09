import paho.mqtt.client as mqtt
import time
import pytest
from publisher import send_mqtt_message, start
from subscriber import proccess_payload

broker_address = "mqtt.eclipseprojects.io"
port = 1883
topic = "reading/solar"

received_messages = []
qos=[]

def on_message(client, userdata, msg):
    print(msg.payload.decode())
    qos.append(msg.qos)
    received_messages.append(proccess_payload(msg))
    
def create_subscriber(broker_address, topic, port):
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(broker_address, port, 60)
    client.subscribe(topic, qos=1)
    return client

def test_subscriber_data():
    print("Testing confirm data sent and data validation")
    payload = '{ "id": "lj01f02", "tipo": "geladeira", "temperatura": 5,"timestamp": "01/03/2024 14:30"}'
    final_msg = 'lj01f02: geladeira | 5°C'

    client = create_subscriber(broker_address,topic, port)

    mqtt_client = start(broker_address, port)

    send_mqtt_message(mqtt_client, topic, payload)

    time.sleep(5)
  
    client.loop_start()
    time.sleep(10)
    client.loop_stop()

    mqtt_client.disconnect()
    client.disconnect()

    print("Received message:", received_messages)

    assert received_messages[0] == final_msg, "Dados inválidos."
    assert qos[0] == 1, "Qos inválido."
