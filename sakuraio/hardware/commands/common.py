import struct
import datetime

# Common
CMD_GET_CONNECTION_STATUS = 0x01
CMD_GET_SIGNAL_QUALITY = 0x02
CMD_GET_DATETIME = 0x03
CMD_ECHO_BACK = 0x0f

CONNECTION_ERROR_NONE = 0x00
CONNECTION_ERROR_OUT_OF_SERVICE = 0x01
CONNECTION_ERROR_CONNECTION = 0x02
CONNECTION_ERROR_DISCONNECTED = 0x03


class CommonMixins(object):

    def get_connection_status(self):
        """Get connection status

        :return: Status. Please see the datasheet.
        :rtype: int
        """
        response = self.execute_command(CMD_GET_CONNECTION_STATUS)
        return response[0]

    def get_is_online(self):
        """Get online

        :return: Weather or not the module is online.
        :rtype: bool
        """

        status = self.get_connection_status()
        return (status & 0x80) == 0x80

    def get_connection_error(self):
        """Get connection error

        :return: Status. Possible values:
            :const:`CONNECTION_ERROR_NONE`, :const:`CONNECTION_ERROR_OUT_OF_SERVICE`,
            :const:`CONNECTION_ERROR_CONNECTION`, :const:`CONNECTION_ERROR_DISCONNECTED`
        :rtype: int
        """
        status = self.get_connection_status()
        return (status & 0x7f)

    def get_signal_quality(self):
        """Get signal quality

        :return: Signal quality. ``0``: out of service. ``5``: most strong.
        :rtype: int
        """
        response = self.execute_command(CMD_GET_SIGNAL_QUALITY)
        return response[0]

    def get_datetime(self):
        """Get current datetime

        :return: Current datetime.
        :rtype: datetime.datetime
        """

        response = self.execute_command(CMD_GET_DATETIME, as_bytes=True)
        unixtime, = struct.unpack("<Q", response)
        return datetime.datetime.utcfromtimestamp(unixtime / 1000.0)

    def echoback(self, values):
        """Test echoback MCU <-> Communication Module

        :param list values:
            List of int values to send.

        :return: Values echoed. It must equals ``values`` param.
        :rtype: list
        """
        response = self.execute_command(CMD_ECHO_BACK, values)
        return response
