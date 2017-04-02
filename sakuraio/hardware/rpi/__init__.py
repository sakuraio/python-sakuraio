from sakuraio.hardware.base import SAKURAIO_SLAVE_ADDR, SakuraIOBase


class SakuraIOSMBus(SakuraIOBase):

    def __init__(self):
        import smbus
        self.bus = smbus.SMBus(1)

    def start(self, write=True):
        if write:
            self.request = []
            self.response = []
        else:
            if self.request:
                self.bus.write_i2c_block_data(SAKURAIO_SLAVE_ADDR, self.request[0], self.request[1:])
            self.response = self.bus.read_i2c_block_data(SAKURAIO_SLAVE_ADDR, 32)

    def send_byte(self, value):
        self.request.append(value)

    def recv_byte(self):
        value = 0x00
        if self.response:
            value = self.response.pop(0)
        return value


class SakuraIOSPI(SakuraIOBase):
    def __init__(self):
        raise NotImplementedError()
