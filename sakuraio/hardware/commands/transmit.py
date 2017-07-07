import struct
import datetime

from .utils import pack

# Transmit
CMD_TX_ENQUEUE = 0x20
CMD_TX_SENDIMMED = 0x21
CMD_TX_LENGTH = 0x22
CMD_TX_CLEAR = 0x23
CMD_TX_SEND = 0x24
CMD_TX_STAT = 0x25


class TransmitMixins(object):

    def enqueue_tx_raw(self, channel, type, values, offset=0):
        """Enqueue channel data by raw values.

        :param int channel:
            Channel number of data. Must be 0 to 127.

        :param string type:
            Type of data. Possible values ``"i"``, ``"I"``, ``"l"``, ``"L"``, ``"f"``, ``"d"`` or ``"b"``.

        :param list values:
            List of int values to enqueue.

        :params int offset:
            Time offset in ms. Default ``0``. It must be less than or equal ``0``.
        """

        values += [0x00] * 8

        if type not in ["i", "I", "l", "L", "f", "d", "b"]:
            raise ValueError("Invalid type '{0}'".format(type))

        request = [channel, ord(type)] + values[:8]
        if offset != 0:
            request += pack("<q", offset)

        self.execute_command(CMD_TX_ENQUEUE, request)

    def send_immediate_raw(self, channel, type, data):
        """Send channel data immediately by raw values.

        :param int channel:
            Channel number of data. Must be 0 to 127.

        :param string type:
            Type of data. Possible values ``"i"``, ``"I"``, ``"l"``, ``"L"``, ``"f"``, ``"d"`` or ``"b"``.

        :param list values:
            List of int values to send.

        """

        data += [0x00] * 8

        if type not in ["i", "I", "l", "L", "f", "d", "b"]:
            raise ValueError("Invalid type '{0}'".format(type))

        request = [channel, ord(type)] + data[:8]
        self.execute_command(CMD_TX_SENDIMMED, request)

    def get_tx_queue_length(self):
        """Get available and queued length of tramsmit queue.

        :return: Size of available and queued data.
        :rtype: dict
        """

        response = self.execute_command(CMD_TX_LENGTH)
        return {
            "available": response[0],
            "queued": response[1],
        }

    def clear_tx(self):
        """Clear transmit queue."""

        self.execute_command(CMD_TX_CLEAR)

    def send(self):
        """Send data in transmit queue."""

        self.execute_command(CMD_TX_SEND)

    def get_tx_status(self):
        """Get status of send

        :return: Status of send.
        :rtype: dict
        """

        response = self.execute_command(CMD_TX_STAT)
        return {
            "queue": response[0],
            "immediate": response[1],
        }
