from machine import Pin
from time import sleep
from neopixel import NeoPixel


class Drumled:

    def __init__(self, data_pin: int, strip_size: int):
        self.led = NeoPixel(Pin(data_pin), strip_size)
        self.N = strip_size

    def test(self):
        for i in range(self.N):
            bri = 1 + round((i / self.N) * 254)
            self.led[i] = (0, 0, bri)
            print('test: ' + 'led' + str(i) + ': ' + str(bri))
            self.led.write()
            sleep(0.2)
        sleep(2)
        self.all()

    def all(self, color=(0, 0, 0)):
        for i in range(self.N):
            self.led[i] = color
        self.led.write()

    def pulse(self, brightness):
        self.all((brightness, 0, 0))
        sleep(0.15)
        self.all((round(brightness / 4), 0, 0))
        sleep(0.05)
        self.all((round(brightness / 20), 0, 0))
