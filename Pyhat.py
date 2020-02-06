from sense_hat import SenseHat
import paho.mqtt.client as mqtt #importamos el cliente
import time
import json

sense = SenseHat()
#variables de entorno
humidity = sense.get_humidity()
temp = sense.get_temperature()
p_bar = sense.get_pressure()

#variables inerciales
orientation = sense.get_orientation_degrees()
compass     = sense.get_compass()
giro        = sense.get_gyroscope()
acce        = sense.get_accelerometer()

#conversion de datos/ algunas funciones retornan un diccionario
# es necesario convertir a str para poder enviarlas por mqtt
giro_s = json.dumps(giro)
orientation_s = json.dumps(orientation)
acce_s = json.dumps(acce)
#print(type(giro_s))

#Enviroment variables
print("Variables ambientales:\nHumity: %s\ntemperature: %s\npressure: %s\n-----------------" %(humidity,temp,p_bar))
#inercial sensors
print("inercial:\norientation:%s\ncompass:%s\ngyroscope:%s\naccelerometer%s\n-------------" %(orientation,compass,giro,acce))


#MQTT CONNECTION
#brokers
broker_1 =  "broker.hivemq.com"
#broker_2 = "iot.eclipse.org"
#topics
tp1 = "hat/giro"
tp2 = "hat/acc"
tp3 = "hat/mag"
tp4 = "hat/p_bar"
tp5 = "hat/temp"
tp6 = "hat/hum"

client = mqtt.Client("pihat")           #instancia of client
print("Conectando al broker",broker_1)
client.connect(broker_1)                #connection

#publish(topic, payload=None, qos=0, retain=False)
client.publish(tp1,giro_s)
client.publish(tp2,acce_s)
client.publish(tp3,orientation_s)
client.publish(tp4,p_bar)
client.publish(tp5,temp)
client.publish(tp6,humidity)
time.sleep(3)

client.disconnect() # desconeccion
