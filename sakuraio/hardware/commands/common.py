import struct
import datetime

# Common
CMD_GET_CONNECTION_STATUS = 0x01
CMD_GET_SIGNAL_QUALITY = 0x02
CMD_GET_DATETIME = 0x03
CMD_ECHO_BACK = 0x0f


class CommonMixins(object):

    def get_connection_status(self):
        response = self.execute_command(CMD_GET_CONNECTION_STATUS)
        return response[0]

    def get_signal_quality(self):
        response = self.execute_command(CMD_GET_SIGNAL_QUALITY)
        return response[0]

    def get_datetime(self):
        response = self.execute_command(CMD_GET_DATETIME, as_bytes=True)
        unixtime, = struct.unpack("<Q", response)
        return datetime.datetime.fromtimestamp(unixtime/1000.0)

    def echoback(self, values):
        response = self.execute_command(CMD_ECHO_BACK, values)
        return response
