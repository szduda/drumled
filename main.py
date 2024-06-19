from machine import Pin, ADC
from led import Drumled
from time import sleep

SENSOR_MAX = 65535
SENSOR_THRESHOLD = 5000
sensor = ADC(Pin(26))

led = Drumled(data_pin=28, strip_size=8)


def read_vibration():
    value = sensor.read_u16()
    if value == SENSOR_MAX:
        print('MAX Vibration read')
    return value


def calc_brightness(sensor_value):
    return round(max(0.0, min(vibration / SENSOR_MAX, 1.0)) * 255)


led.test()

while True:
    vibration = read_vibration()

    if vibration > SENSOR_THRESHOLD:
        brightness = calc_brightness(vibration)
        print("New Brightness: " + str(brightness))
        led.pulse(brightness)
