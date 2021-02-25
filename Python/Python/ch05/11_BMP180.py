import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

temp = sensor.read_temperature()
presure = sensor.read_pressure()
altitude = sensor.read_altitude()

print('Temp = {0:0.2f} *C' .format(temp))
print('Presure = {0:0.2f} Pa' .format(presure))
print('Altitude = {0:0.2f} m' .format(altitude))
