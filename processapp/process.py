import paho.mqtt.client as mqtt
import json
import boto3
import datetime
from influxdb import InfluxDBClient


# The callback for when the client receives a connection response from the server.
def on_connect(client, userdata, flags, rc):
    client.subscribe("carCoordinates")

# the callback for when the client receives a message response
def on_message(client, userdata, msg):

    json_dict=json.loads(msg.payload)
    car_index=json_dict['carIndex']
    location_lat=json_dict['location']['lat']
    location_long=json_dict['location']['long']
    timestamp=json_dict['timestamp']
    
    clientdb = InfluxDBClient(host="influxdb", port=8086, username="admin", password="admin")
    clientdb.switch_database('mclarenDB')

    json_body = [
            {
                "measurement": "carCoordinates",
                "tags": { "Topic": str(msg.topic)},
                "time": str(datetime.datetime.now()),
                "fields": {
                    "carIndex": car_index,
                    "location_lat": location_lat,
                    "location_long": location_long,
                    "timestamp": timestamp
                    }
                }
            ]

    clientdb.write_points(json_body)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker", 1883, 60)
client.loop_forever()
