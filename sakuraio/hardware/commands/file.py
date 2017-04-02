import struct
import datetime

# File Download
CMD_START_FILE_DOWNLOAD = 0x40
CMD_GET_FILE_METADATA = 0x41
CMD_GET_FILE_DOWNLOAD_STATUS = 0x42
CMD_CANCEL_FILE_DOWNLOAD = 0x43
CMD_GET_FILE_DATA = 0x44


class FileMixins(object):
    pass
