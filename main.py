from machine import I2C, Pin
from time import sleep_ms
from apds9900LITE import APDS9900LITE

#Init I2C Buss on RP2040
i2c = I2C(0, scl=Pin(7), sda=Pin(6), freq=400_000)
onboardled= Pin(8, Pin.OUT)

apds9900=APDS9900LITE(i2c)      # Enable sensor
apds9900.prox.enableSensor()    # Enable Proximit sensing

while True:
        sleep_ms(25) # wait for readout to be ready
        print(apds9900.prox.proximityLevel)   #Print the proximity value
        if apds9900.prox.proximityLevel > 110:
            onboardled.value(0) # LED on ESP32-C3 super mini has its logic inverted
        else:
            onboardled.value(1)

 