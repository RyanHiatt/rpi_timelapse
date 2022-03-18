import datetime
import time
import glob
import os
import picamera

from devicemanager import DeviceManager


camera = picamera.PiCamera()
device_manager = DeviceManager()

if device_manager.check_for_usb():
    list_of_images = glob.glob(f"{device_manager.usb_path}/*.jpg")
    latest_file = max(list_of_images, key=os.path.getctime)
    file_index = int(latest_file.split('.')[0].split('e')[1])

    i = file_index + 1
    while True:
        camera.capture(f"{device_manager.usb_path}/image{i:08d}.jpg")  # image00000001.jpg
        if device_manager.check_usb_capacity() < 10:
            break
        else:
            i += 1
            time.sleep(1)
