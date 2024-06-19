from machine import Pin, ADC
from neopixel import NeoPixel
from time import sleep

sensor = ADC(Pin(26))

ledPin = Pin(28)
N = 8
MAX = 65535
led = NeoPixel(ledPin, N)

# for i in range(N):
#     led[i] = (0, 100, (i / N) * 255)
#     led.write()
#     sleep(0.2)
#
# sleep(10)

for i in range(N):
    led[i] = (0, 20, 10)
    led.write()
    sleep(0.3)

# sleep(2)

# while True:
#     vibration = sensor.read_u16()
#     if vibration == MAX:
#         print('max sensor read')
#     # if 1000 < vibration < MAX:
#     #     print(vibration)
#
#     if vibration > 1000:
#         brightness = round(max(0.05, min(vibration / MAX, 1.0)) * 255)
#         print(brightness)
#         for i in range(N):
#             led[i] = (brightness, 0, 0)
#         led.write()
#         sleep(0.15)
#         for i in range(N):
#             led[i] = (round(brightness / 4), 0, 0)
#         led.write()
#         sleep(0.05)
#         for i in range(N):
#             led[i] = (round(brightness / 20), 0, 0)
#         led.write()
