import paho.mqtt.client as mqtt
import json
import boto3
import time

timestream = boto3.client('timestream-write', region_name='eu-west-1')
database_name='mclarenDB'
table_name='mclarentable'




# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("carCoordinates")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    json_dict=json.loads(msg.payload)
    car_index=json_dict['carIndex']
    location_lat=json_dict['location']['lat']
    location_long=json_dict['location']['long']
    timestamp=json_dict['timestamp']
   
    #data prep for timestream
    timestream_prep(str(msg.topic), car_index, location_lat, location_long, timestamp)

    #send data to aws timestream
    try:

        response =timestream.write_records(
                DatabaseName=database_name,
                TableName=table_name,
                CommonAttributes=CommonAttributes,
                Records=records)

    except timestream.exceptions.RejectedRecordsException as err:
        print({'exception': err})
        for rejected in err.response['RejectedRecords']:
            print({'reason': rejected['Reason'],
                   'rejected_record': records[rejected['RecordIndex']] })




def timestream_prep(topic, car_i, location_lat, location_long, ts):

    dimensions = [{'Name': 'Topic',
                   'Value': str(topic),
                   }]
    CommonAttributes={'Dimensions': dimensions,
                      'MeasureValueType': 'VARCHAR',
                      'Time': str(int(time.time())),
                          'TimeUnit': 'SECONDS'}

    carIndex={'MeasureName': 'carIndex',
              'MeasureValue': str(car_i)}

    lat_loc={'MeasureName': 'lat_location',
             'MeasureValue': str(location_lat)}
    long_loc={'MeasureName': 'long_location',
             'MeasureValue': str(location_long)}
    timeStamp={'MeasureName': 'timestamp',
               'MeasureValue': str(ts)}

    records= [carIndex, lat_loc, long_loc, timeStamp]

    return records

def publish_prep(car_index, location_lat, location_long, timestamp):

    cs_message={
                'timestamp': timestamp,
                'carIndex': car_index,
                'type': str

        


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker", 1883, 60)
client.loop_forever()
