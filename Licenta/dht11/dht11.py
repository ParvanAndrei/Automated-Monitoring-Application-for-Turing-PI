#!/usr/bin/python
import Adafruit_DHT
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from statistics import mean


token = os.environ['token']
syst = os.environ['name']
org = "andrei.parvan81@gmail.com"
url = "https://europe-west1-1.gcp.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="DB"
write_api = client.write_api(write_options=SYNCHRONOUS)

dataset_list_temperature = []
dataset_list_humidity = []


while True:
	humidity, temperature = Adafruit_DHT.read_retry(11,4)
#	file = open("measures.txt","a" )
	# print(temperature)
#	file.write('Temp: {0:0.1f} C Humidity: {1:0.1f} %  \n'.format(temperature,humidity))
	dataset_list_temperature.append(temperature)
	dataset_list_humidity.append(humidity)
	if len(dataset_list_humidity) == 60 and len(dataset_list_temperature) ==60:
		humidity_avg = mean(dataset_list_humidity)
		temperature_avg = mean(dataset_list_temperature)
		dataset_list_humidity.clear()
		dataset_list_temperature.clear()
		point = (
		  Point("DHT11-" + syst)
		  .field("Temperature",temperature_avg )
		  .field("Humidity", humidity_avg)
	  	)
		write_api.write(bucket=bucket, org="andrei.parvan81@gmail.com", record=point)
#	time.sleep(330)
	time.sleep(10)

