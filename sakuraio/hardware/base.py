import datetime
import struct

from sakuraio.hardware.commands import CommandMixins, CMD_ERROR_NONE
from sakuraio.hardware.exceptions import CommandError, ParityError

SAKURAIO_SLAVE_ADDR = 0x4f


def calc_parity(values):
    parity = 0x00
    for value in values:
        parity ^= value
    return parity


class SakuraIOBase(CommandMixins):

    def start(self, write=True):
        return

    def end(self):
        return

    def send_byte(self, value):
        raise NotImplementedError()

    def recv_byte(self):
        raise NotImplementedError()

    def execute_command(self, cmd, request=[], as_bytes=False):
        response = []

        request = [cmd, len(request)] + request
        request.append(calc_parity(request))

        try:
            # Request
            self.start(True)
            for value in request:
                self.send_byte(value)

            # Response
            self.start(False)
            status = self.recv_byte()
            if status != CMD_ERROR_NONE:
                raise CommandError(status)

            length = self.recv_byte()
            response = []
            for i in range(length):
                response.append(self.recv_byte())
            parity = self.recv_byte()

            if parity != calc_parity([status, length] + response):
                raise ParityError()

        except:
            self.end()
            raise

        self.end()

        if as_bytes:
            return struct.pack("B" * len(response), *response)
        return response
