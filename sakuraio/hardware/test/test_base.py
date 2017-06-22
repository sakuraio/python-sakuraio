import unittest
from unittest import mock

from sakuraio.hardware.base import calc_parity
from sakuraio.hardware.dummy import DummySakuraIO
from sakuraio.hardware.exceptions import CommandError, ParityError


class SakuraIOBaseTest(unittest.TestCase):

    def test_parity(self):
        self.assertEqual(calc_parity([0x00]), 0x00)
        self.assertEqual(calc_parity([0x24]), 0x24)
        self.assertEqual(calc_parity([0x00, 0x24]), 0x24)
        self.assertEqual(calc_parity([0x24, 0x24]), 0x00)
        self.assertEqual(calc_parity([0x00, 0x01, 0xa2, 0x33]), 0x90)

    def _execute_command(self, cmd, request, response, as_bytes=False):
        base = DummySakuraIO()
        base.initial(response)
        return base.execute_command(cmd, request, as_bytes=as_bytes)

    def test_execute_command(self):
        base = DummySakuraIO()

        cmd = 0x10
        request = [0x01, 0x02, 0x03, 0x04]
        request.append(calc_parity(request))

        response = [0x01, 0x04, 0x11, 0x12, 0x13, 0x14]
        response.append(calc_parity(response))

        expected = response[2:-1]

        self.assertEqual(self._execute_command(cmd, request, response), expected)

    def test_execute_command_status_error(self):
        base = DummySakuraIO()

        cmd = 0x10
        request = [0x01, 0x02, 0x03, 0x04]
        request.append(calc_parity(request))

        status = 0x02
        response = [status, 0x00]
        response.append(calc_parity(response))

        with self.assertRaises(CommandError):
            self._execute_command(cmd, request, response)

    def test_execute_command_parity_error(self):
        base = DummySakuraIO()

        cmd = 0x10
        request = [0x01, 0x02, 0x03, 0x04]
        request.append(calc_parity(request))

        status = 0x01
        response = [status, 0x00]
        response.append(0x12)

        with self.assertRaises(ParityError):
            self._execute_command(cmd, request, response)
