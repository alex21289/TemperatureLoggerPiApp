# TemperatureLoggerPiApp
A simple script to log temperature and humidity from a DHT22 sensor on a Raspberry Pi.
The data will stored in a SQL-database. In this case a postgres db on the Rasperry Pi with Ubuntu Server 18.

The data are displayed with a simple flask app using the chart.js libary, which you can find here:
- https://github.com/alex21289/TemperatureLoggerWebApp

## Requirements

- https://github.com/adafruit/Adafruit_Python_DHT
