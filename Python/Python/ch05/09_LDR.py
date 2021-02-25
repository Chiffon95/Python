import spidev
import time

spi = spidev.SpiDev()

spi.open(0,0)

spi.max_speed_hz = 100000

delay = 0.5

pot_channel = 0

def readadc(adcnum):
   if adcnum > 7 or adcnum<0:
      return -1
   r = spi.xfer2([1,(8+adcnum)<<4,0])
   data = ((r[1]&3) << 8) + r[2]
   return data

while True:
   value = readadc(pot_channel)
   read_voltage = value * 3.3/1024
   print("----------------------")
   print("value : %d read vlotage : %f" % (value,read_voltage))
   time.sleep(delay)
