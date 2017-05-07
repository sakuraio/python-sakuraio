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


PRODUCT_ID_SCM_LTE_BETA = 0x01
PRODUCT_ID_SCM_LTE_01 = 0x02

PRODUCT_ID_MAP = {
    PRODUCT_ID_SCM_LTE_BETA: "SCM-LTE-BETA",
    PRODUCT_ID_SCM_LTE_01: "SCM-LTE-01",
}


class OperationMixins(object):

    def get_product_id(self):
        """Get product id

        :return: Product ID. Possible values:
            :const:`PRODUCT_ID_SCM_LTE_BETA`, :const:`PRODUCT_ID_SCM_LTE_01`
        :rtype: int
        """

        response = self.execute_command(CMD_GET_PRODUCT_ID, as_bytes=True)
        product_id = struct.unpack("<H", response)[0]
        return product_id

    def get_product_name(self):
        """Get product name

        :return: Product name. Possible values: ``"SCM-LTE-BETA"``, ``"SCM-LTE-01"``.
        :rtype: str
        """

        product_id = self.get_product_id()
        return PRODUCT_ID_MAP.get(product_id, "{0:04X}".format(product_id))

    def get_unique_id(self):
        """Get unique id

        :return: Unique ID. For example `"16X0000001"``.
        :rtype: str
        """

        return self.execute_command(CMD_GET_UNIQUE_ID, as_bytes=True).decode("ascii")

    def get_firmware_version(self):
        """Get firmware version

        :return: Firmware version. For example `"v1.1.2-170223-7e6ce64"``.
        :rtype: str
        """
        return self.execute_command(CMD_GET_FIRMWARE_VERSION, as_bytes=True).decode("ascii")

    def unlock(self):
        """Unlock critical command"""

        self.execute_command(CMD_UNLOCK, UNLOCK_MAGIC_NUMBERS)

    def update_firmware(self):
        """Request to update firmware"""
        self.execute_command(CMD_UPDATE_FIRMWARE)

    def get_firmware_update_status(self):
        """Get firmware update status

        :return: Status.
        :rtype: dict
        """

        response = self.execute_command(CMD_GET_FIRMWARE_UPDATE_STATUS)[0]
        inprogress = (response & 0x80) == 0x80
        return {
            "inprogress": inprogress,
            "error": response & 0x7f,
        }

    def reset(self):
        """Request software reset"""

        self.execute_command(CMD_SOFTWARE_RESET)
