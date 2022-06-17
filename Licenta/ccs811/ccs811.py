#!/usr/bin/python
import board
import adafruit_ccs811
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from statistics import mean


i2c = board.I2C()
ccs811 = adafruit_ccs811.CCS811(i2c)

org = "andrei.parvan81@gmail.com"
url = "https://europe-west1-1.gcp.cloud2.influxdata.com"
token = os.environ['token']
syst = os.environ['name']
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="DB"
write_api = client.write_api(write_options=SYNCHRONOUS)


dataset_list_co2 = []
dataset_list_tvoc = []


while not ccs811.data_ready:
	pass
time.sleep(1)
while True:
	dataset_list_co2.append(ccs811.eco2)
	dataset_list_tvoc.append(ccs811.tvoc)
	if len(dataset_list_co2)==60 and len(dataset_list_tvoc)==60:
		co2_avg = mean(dataset_list_co2)
		tvoc_avg = mean(dataset_list_tvoc)
		dataset_list_co2.clear()
		dataset_list_tvoc.clear()
		point = (
		  Point("CCS811- "+ syst )
		  .field("CO2",co2_avg )
		  .field("TVOC", tvoc_avg)
	  	)
		write_api.write(bucket=bucket, org="andrei.parvan81@gmail.com", record=point)
#	time.sleep(330)
	time.sleep(10)

