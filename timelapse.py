import datetime
import time
import picamera

from devicemanager import DeviceManager


camera = picamera.PiCamera()
device_manager = DeviceManager()

if device_manager.check_for_usb():

    i = 0
    while True:
        camera.capture(f"{device_manager.usb_path}/image{i:08d}.jpg")
        if device_manager.check_usb_capacity() < 10:
            break
        else:
            i += 1
            time.sleep(1)
