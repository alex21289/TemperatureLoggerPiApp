import modules.measure_dht22 as dht22
from modules.csv import csv
import datetime as dt
import psycopg2
#import RPi.GPIO

# Database
db="temppy"
username="temppy"
password=""
host="127.0.0.1"
port="5432"

conn = psycopg2.connect(database=db, user=username,password=password, host=host, port=port)

print ("Opened database successfully")
curs = conn.cursor()

datum = dt.datetime.now().date()
zeit = dt.datetime.now()

def main():
    sensor = dht22.Adafruit_DHT.DHT22
    pin = 4
    print("Temperatursensor auslesen")
    sensor1=dht22.Measure(sensor,pin) # neue Instanz der Klasse Measure() aus dem Modul erzeugen. SensorModell=22, GPIO_Pi=4
    humidity, temperature = sensor1.read_temperature()
    humidity = '{:.2f}'.format(humidity)
    temperature = '{:.2f}'.format(temperature)
    print("Lustfeuchtigkeit: "+humidity)
    print("Temperatur: "+temperature)
    try:
        curs.execute ("INSERT INTO temperature(TIME,HUMIDITY, TEMP) VALUES (%s,%s, %s);", (zeit,humidity, temperature))
        conn.commit()
        print("Daten übertragen")
    except Exception as e:
        print("Fehler: ")
        print(e)


    #curs.execute("SELECT * FROM temperature;")
    #liste=curs.fetchall()
    #for row in liste:
       #print(row[1].strftime("%d.%m.%y"))

    curs.close()
    conn.close()
    
    


if __name__=='__main__':
    main()
