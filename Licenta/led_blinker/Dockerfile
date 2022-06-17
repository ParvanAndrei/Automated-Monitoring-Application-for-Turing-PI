FROM arm32v7/python:3.7-slim-buster

COPY led_blinker.py ./

RUN apt-get update && \
    apt-get -y install gcc mono-mcs

RUN pip3 install rpi.gpio

CMD ["python3", "./led_blinker.py"]
