FROM arm32v7/python:3.7-slim-buster

COPY dht11.py ./

RUN apt-get -y update && \
    apt-get -y install git-core && \
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git && \
    apt-get -y install build-essential python-dev && \
    cd Adafruit_Python_DHT && \
    python3 setup.py install

#RUN pip3 install rpi.gpio

CMD ["python3", "dht11.py"]
