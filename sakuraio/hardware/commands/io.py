import struct
import datetime

# IO
CMD_READ_ADC = 0x10


class IOMixins(object):

    def get_adc(self, channel):
        response = self.execute_command(CMD_READ_ADC, [channel], as_bytes=True)
        value, = struct.unpack("<L", response)
        return value
