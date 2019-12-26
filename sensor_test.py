import Adafruit_DHT


sensor = Adafruit_DHT.DHT22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
print(temperature)
temperature = '{:.2f}'.format(temperature)
print(temperature)
