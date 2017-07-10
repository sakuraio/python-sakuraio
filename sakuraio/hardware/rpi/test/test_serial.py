import unittest

from sakuraio.hardware.rpi import SakuraIOSerial

try:
    from unittest import mock
except ImportError:
    import mock


class DummySerial(object):

    def __init__(self):
        self.send_buffer = b""
        self.read_buffer = b""

    def read(self):
        c = b""
        if self.read_buffer:
            c = self.read_buffer[0:1]
            self.read_buffer = self.read_buffer[1:]
        return c

    def write(self, s):
        self.send_buffer += s

    def close(self):
        pass


class SerialTest(unittest.TestCase):

    def test_get_unique_id(self):

        with mock.patch('serial.Serial') as serial:
            sakuraio = SakuraIOSerial("dummy")
            sakuraio.serial = DummySerial()

            sakuraio.serial.read_buffer = "OK\r\n*CMD:010A313642303130303236307B\r\nOK\r\n".encode("ascii")
            self.assertEqual(sakuraio.get_unique_id(), "16B0100260")
            self.assertEqual(sakuraio.serial.send_buffer, "AT*CMD=A100A1\n".encode("ascii"))
