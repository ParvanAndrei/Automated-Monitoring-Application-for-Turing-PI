#!/usr/bin/python
import adafruit_bme680
import board
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from statistics import mean


# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

org = "andrei.parvan81@gmail.com"
url = "https://europe-west1-1.gcp.cloud2.influxdata.com"
token = os.environ['token']
syst = os.environ['name']
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="DB"
write_api = client.write_api(write_options=SYNCHRONOUS)



# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25
dataset_list_temperature = []
dataset_list_relative_humidity = []
dataset_list_gas = []
dataset_list_pressure = []
dataset_list_altitude = []

# You will usually have to add an offset to account for the temperature of
# the sensor. This is usually around 5 degrees but varies by use. Use a
# separate temperature sensor to calibrate this one.
# temperature_offset = -5

while True:
    dataset_list_temperature.append(bme680.temperature)
    dataset_list_relative_humidity.append(bme680.relative_humidity)
    dataset_list_gas.append(bme680.gas)
    dataset_list_pressure.append(bme680.pressure)
    dataset_list_altitude.append(bme680.altitude)
    if len(dataset_list_temperature)==60 and len(dataset_list_relative_humidity)==60 and len(dataset_list_gas)==60 and len(dataset_list_pressure)==60 and len(dataset_list_altitude)==60:
        temperature_avg = mean(dataset_list_temperature)
        relative_humidity_avg = mean(dataset_list_relative_humidity)
        gas_avg = mean(dataset_list_gas)
        pressure_avg = mean(dataset_list_pressure)
        altitude_avg = mean(dataset_list_altitude)
        dataset_list_temperature.clear()
        dataset_list_relative_humidity.clear()
        dataset_list_gas.clear()
        dataset_list_pressure.clear()
        dataset_list_altitude.clear()
        point = (
    	  Point("BME680- "+syst)
    	  .field("Temperature",temperature_avg )
    	  .field("Humidity",relative_humidity_avg )
    	  .field("Gas",gas_avg )
    	  .field("Pressure",pressure_avg )
    	  .field("Altitude", altitude_avg)
      	)
        write_api.write(bucket=bucket, org="andrei.parvan81@gmail.com", record=point)
#	time.sleep(330)
    time.sleep(10)
