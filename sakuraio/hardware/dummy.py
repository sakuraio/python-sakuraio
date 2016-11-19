from sakuraio.hardware.base import SakuraIOBase


class DummySakuraIO(SakuraIOBase):

    def start(self, write=True):
        pass

    def end(self):
        pass

    def initial(self, response):
        self.return_values = response
        self.values = []

    def send_byte(self, value):
        self.values.append(value)

    def recv_byte(self):
        value = self.return_values[0]
        self.return_values = self.return_values[1:]
        return value
