import picamera
from picamera import Color
import time

with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (640, 480)
    camera.start_preview()
    #camera.image_effect = 'sketch'
    camera.exposure_mode = 'auto'
    camera.annotate_background = Color('black')
    camera.annotate_foreground = Color('white')
    for i in range(5):
        camera.annotate_text = ('raspi camera testtttttting + %s' %i)
        time.sleep(1)
        camera.capture('/home/pi/chiffona/Python/Python/ch08/rpi_still%s.jpg' % i)
    camera.stop_preview()