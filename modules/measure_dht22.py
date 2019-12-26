#/usr/bin/python3

# Bib zum auslesen des DHT22 Temperatur- und Luftfeuchtigkeitssenor

import Adafruit_DHT
import time

class Measure():

    def __init__(self,sensor, pin):
        self.sensor = sensor
        self.pin = pin

    def read_test(self):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            if humidity is not None and temperature is not None:
                print("Temperatur: {0:0.1f} °C".format(temperature))
                print("Luftfeuchtigkeit: {0:0.1f}%".format(humidity))
            else:
                print("Lesen fehlgeschlagen...")
        except Exception as e:
            print("excpet Anweisung eingeleitet")
            print("\n")
            print(e)
            print("Eventuell root Rechte benötigt, versuche es mit sudo")

    def read_temperature(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin) #Gibt einen Tupel zurück, werte des tupesl werden in beide Variablen als float übergeben
        return humidity,temperature

