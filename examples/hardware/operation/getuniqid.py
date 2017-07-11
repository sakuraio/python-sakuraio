from sakuraio.hardware.rpi import SakuraIOGPIO
#from sakuraio.hardware.rpi import SakuraIOSMBus
import time

sakuraio = SakuraIOGPIO()
#sakuraio = SakuraIOSMBus()

print(sakuraio.get_unique_id())
time.sleep(3)
print(sakuraio.get_firmware_version())


