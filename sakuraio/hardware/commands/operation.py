import struct
import datetime

# Operation
CMD_GET_PRODUCT_ID = 0xA0
CMD_GET_UNIQUE_ID = 0xA1
CMD_GET_FIRMWARE_VERSION = 0xA2
CMD_UNLOCK = 0xA8
CMD_UPDATE_FIRMWARE = 0xA9
CMD_GET_FIRMWARE_UPDATE_STATUS = 0xAA
CMD_SOFTWARE_RESET = 0xAF

UNLOCK_MAGIC_NUMBERS = [0x53, 0x6B, 0x72, 0x61]


class OperationMixins(object):

    def get_product_id(self):
        response = self.execute_command(CMD_GET_PRODUCT_ID, as_bytes=True)
        return struct.unpack("<H", response)[0]

    def get_unique_id(self):
        return self.execute_command(CMD_GET_UNIQUE_ID, as_bytes=True).decode("ascii")

    def get_firmware_version(self):
        return self.execute_command(CMD_GET_FIRMWARE_VERSION, as_bytes=True).decode("ascii")

    def unlock(self):
        self.execute_command(CMD_UNLOCK, UNLOCK_MAGIC_NUMBERS)

    def update_firmware(self):
        self.execute_command(CMD_UPDATE_FIRMWARE)

    def get_firmware_update_status(self):
        response = self.execute_command(CMD_GET_FIRMWARE_UPDATE_STATUS)[0]
        has_error = (response & 0x80) == 0x80
        return {
            "has_error": has_error,
            "status": response & 0x7f,
        }

    def reset(self):
        self.execute_command(CMD_SOFTWARE_RESET)
