import paho.mqtt.publish as publish

BROKER = "broker.hivemq.com"


def enviar_mqtt(topic, mensaje):
    publish.single(topic, mensaje, hostname=BROKER)
