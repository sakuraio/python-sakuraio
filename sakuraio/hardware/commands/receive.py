import struct
import datetime

# Receive
CMD_RX_DEQUEUE = 0x30
CMD_RX_PEEK = 0x31
CMD_RX_LENGTH = 0x32
CMD_RX_CLEAR = 0x33


class ReceiveMixins(object):

    def dequeue_rx_raw(self):
        """Dequeue received data

        :return: Dict of received data.
        :rtype: dict
        """

        response = self.execute_command(CMD_RX_DEQUEUE)
        return {
            "channel": response[0],
            "type": chr(response[1]),
            "data": response[2:10],
            "offset": struct.unpack("<q", struct.pack("8B", *response[10:18]))[0],
        }

    def peek_rx_raw(self):
        """Peek received data

        :return: Dict of received data.
        :rtype: dict
        """

        response = self.execute_command(CMD_RX_PEEK)
        return {
            "channel": response[0],
            "type": chr(response[1]),
            "data": response[2:10],
            "offset": struct.unpack("<q", struct.pack("8B", *response[10:18]))[0],
        }

    def get_rx_queue_length(self):
        """Get available and queued length of receive queue.

        :return: Size of available and queued data.
        :rtype: dict
        """

        response = self.execute_command(CMD_RX_LENGTH)
        return {
            "available": response[0],
            "queued": response[1],
        }

    def clear_rx(self):
        """Clear receive queue."""

        self.execute_command(CMD_RX_CLEAR)
