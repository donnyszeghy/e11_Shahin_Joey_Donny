import adafruit_bme680
import adafruit_pm25
from adafruit_pm25.uart import PM25_UART
import sys
import time
import board
import csv
import serial
import matplotlib.pyplot as plt


start_time = time.time()
now = start_time

#run_time = 30
run_time = int(sys.argv[1])

#filename = "week5_lab_data.csv"
filename = sys.argv[2]


# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

reset_pin=None
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)
pm25 = PM25_UART(uart, reset_pin)


file = open(filename, 'w', newline='')
writer = csv.writer(file)

meta_data = ['Time', 'pm25', 'pm10', 'Temperature', 'Pressure', 'Humidity', 'Altitude', 'Gas']
writer.writerow(meta_data)


while (now - start_time) < run_time:
    
    time.sleep(1)
    aqdata = pm25.read()
    
    data25um = aqdata["particles 25um"]
    data10um = aqdata["particles 10um"]

    temp = bme680.temperature
    hum = bme680.relative_humidity
    press = bme680.pressure
    alt = bme680.altitude
    gas = bme680.gas
    
    now = time.time()
    datalist = [now, data25um, data10um, temp, press, hum, alt, gas]
    writer.writerow(datalist)
    print(datalist)

file.close()
