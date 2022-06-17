import RPi.GPIO as GPIO
import time
import sys
import os


# ca sa rulezi scriptul ai nevoie de argumentul [1] cu numarul pinului in comanda din terminal
LED_PIN = os.environ['test']
print(LED_PIN)

# Configure the PIN # 8
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(int(sys.argv[1]), GPIO.OUT)
GPIO.setup(int(LED_PIN), GPIO.OUT)
GPIO.setwarnings(False)
#GPIO.setup(16,GPIO.OUT)

# Blink Interval 
blink_interval = .5 #Time interval in Seconds

# Blinker Loop
while True:
# GPIO.output(int(sys.argv[1]), True)
 GPIO.output(int(LED_PIN), True)
# GPIO.output(16,True)
 print("true")
 time.sleep(blink_interval)
# GPIO.output(int(sys.argv[1]), False)
 GPIO.output(int(LED_PIN), False)
# GPIO.output(16,False)
 print("false")
 time.sleep(blink_interval)

# Release Resources
GPIO.cleanup()
