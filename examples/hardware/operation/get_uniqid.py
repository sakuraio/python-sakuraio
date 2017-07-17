from sakuraio.hardware.rpi import SakuraIOGPIO
import time

sakuraio = SakuraIOGPIO()

print(sakuraio.get_unique_id())
time.sleep(3)
print(sakuraio.get_firmware_version())
