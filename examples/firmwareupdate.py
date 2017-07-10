from sakuraio.hardware.rpi import SakuraIOGPIO
#from sakuraio.hardware.rpi import SakuraIOSMBus
import time

sakuraio = SakuraIOGPIO()
#sakuraio = SakuraIOSMBus()

sakuraio.unlock()
time.sleep(1)
sakuraio.update_firmware()

#print(sakuraio.get_firmware_version())


