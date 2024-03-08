import paho.mqtt.client as mqtt
import json
broker_address = "mqtt.eclipseprojects.io"
port = 1883
topic = "reading/temp" 

def on_message(client, userdata, payload):
    # Lj 1: Freezer   1 | -18°C
    print(proccess_payload(payload))

def proccess_payload(msg):
    _msg= json.loads(msg.payload.decode())
    _alert_high=" [ALERTA: Temperatura ALTA]"
    _alert_low=" [ALERTA: Temperatura BAIXA]"
  
    _id = _msg["id"]
    _tipo = _msg["tipo"]
    _temp= _msg["temperatura"]

    _final_msg=f"{_id}: {_tipo} | {_temp}°C"

    if _tipo=="freezer":
       if _temp>-15:
           _final_msg+=_alert_high
       if _temp<-25:
           _final_msg+=_alert_low
    elif _tipo=="geladeira":
       if _temp>10:
           _final_msg+=_alert_high
       if _temp<2:
           _final_msg+=_alert_low

    return _final_msg

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic, qos=1)
    print(f"Inscrito no tópico '{topic}'\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port, 60)
client.loop_forever()