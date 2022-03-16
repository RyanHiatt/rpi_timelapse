import os
import shutil
import psutil


class DeviceManager:

    usb_path = ''
    usb_status = False

    def check_usb_capacity(self):
        total, used, free = shutil.disk_usage(self.usb_path)

        print("USB Drive Capacity Check:\n"
              f"\tTotal: {total // 1048576} MiB\n"
              f"\tUsed: {used // 1048576} MiB\n"
              f"\tFree: {free // 1048576} MiB")

        return free // 1048576  # In MiB

    def check_for_usb(self):
        devices = [device for device in psutil.disk_partitions()]
        usb_result = next((device for device in devices if 'sda' in device.device), False)

        if usb_result:
            if self.usb_status:
                pass
            else:
                self.usb_status = True
                self.usb_path = usb_result.mountpoint
                print(f"USB drive found: {usb_result.device}")
        else:
            if self.usb_status:
                self.eject_usb()
            else:
                print("USB drive not found")

        return self.usb_status

    def eject_usb(self):
        try:
            if self.usb_path == "/":
                print("USB drive eject failure: path is '/'")
                self.usb_status = False
                return False
            else:
                os.system(f"sudo umount -l {self.usb_path}")
                self.usb_status = False
                print("USB drive unmounted")
                return True

        except PermissionError as e:
            print(f"USB ejection error: {e}")
            return False
