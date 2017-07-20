from sakuraio.hardware.rpi import SakuraIOGPIO
import time

sakuraio = SakuraIOGPIO()

try:
    unique_id = sakuraio.get_unique_id()
    print(unique_id)
except:
    raise Exception()

time.sleep(3)

try:
    firm_version = sakuraio.get_firmware_version()
    print(firm_version)
except:
    raise Exception()
