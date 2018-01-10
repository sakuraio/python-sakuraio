import unittest

from sakuraio.hardware.commands.utils import value_to_bytes

class UtilsTest(unittest.TestCase):

    def test_value_to_bytes(self):
        self.assertEqual(value_to_bytes(0x12345678), ('l', [0x78, 0x56, 0x34, 0x12, 0x00, 0x00, 0x00, 0x00]))
        self.assertEqual(value_to_bytes(-1), ('l', [255, 255, 255, 255, 255, 255, 255, 255]))
        self.assertEqual(value_to_bytes(9223372036854775807), ('l', [255, 255, 255, 255, 255, 255, 255, 127]))
        self.assertEqual(value_to_bytes(9223372036854775808), ('L', [0, 0, 0, 0, 0, 0, 0, 128]))
        self.assertEqual(value_to_bytes(3.14), ('d', [31, 133, 235, 81, 184, 30, 9, 64]))
        self.assertEqual(value_to_bytes("Hello"), ('b', [72, 101, 108, 108, 111, 0, 0, 0]))
        self.assertEqual(value_to_bytes("Hello World"), ('b', [72, 101, 108, 108, 111, 32, 87, 111]))
        self.assertEqual(value_to_bytes(b"Hello"), ('b', [72, 101, 108, 108, 111, 0, 0, 0]))
