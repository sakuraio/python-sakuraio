import struct
import datetime

# Transmit
CMD_TX_ENQUEUE = 0x20
CMD_TX_SENDIMMED = 0x21
CMD_TX_LENGTH = 0x22
CMD_TX_CLEAR = 0x23
CMD_TX_SEND = 0x24
CMD_TX_STAT = 0x25


class TransmitMixins(object):

    def enqueue_tx_raw(self, channel, type, data, offset=0):
        data += [0x00] * 8

        if type not in ["i", "I", "l", "L", "f", "d", "b"]:
            raise ValueError("Invalid type '{0}'".format(type))

        request = [channel, ord(type)] + data[:8]
        if offset != 0:
            request += struct.pack("<q", offset)

        self.execute_command(CMD_TX_ENQUEUE, request)

    def enqueue_tx_immediate_raw(self, channel, type, data):
        data += [0x00] * 8

        if type not in ["i", "I", "l", "L", "f", "d", "b"]:
            raise ValueError("Invalid type '{0}'".format(type))

        request = [channel, ord(type)] + data[:8]
        self.execute_command(CMD_TX_SENDIMMED, request)

    def get_tx_queue_length(self):
        response = self.execute_command(CMD_TX_LENGTH)
        return {
            "available": response[0],
            "queued": response[1],
        }

    def clear_tx(self):
        self.execute_command(CMD_TX_CLEAR)

    def send(self):
        self.execute_command(CMD_TX_SEND)

    def get_tx_status(self):
        response = self.execute_command(CMD_TX_STAT)
        return {
            "queue": response[0],
            "immediate": response[1],
        }
