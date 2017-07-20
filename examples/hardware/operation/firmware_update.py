from sakuraio.hardware.rpi import SakuraIOGPIO
import time

sakuraio = SakuraIOGPIO()

print("current version is {0}".format(sakuraio.get_firmware_version()))

sakuraio.unlock()

time.sleep(1)

try:
    sakuraio.update_firmware()
except:
    raise Exception()

print("updated version is {0}".format(sakuraio.get_firmware_version()))
