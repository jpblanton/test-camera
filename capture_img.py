import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2) # wake up
    for filename in camera.capture_continuous('img{timestamp}.jpg'):
        print('Captured %s' % filename)
        time.sleep(60) # wait 5 minutes
