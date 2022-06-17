FROM arm32v7/python:3.7-slim-buster
COPY bme680.py ./
RUN apt-get -y update
RUN apt-get -y install build-essential python-dev
RUN pip3 install influxdb-client
RUN pip3 install RPi.GPIO
RUN pip3 install adafruit-circuitpython-bme680
CMD ["python3", "bme680.py"]
