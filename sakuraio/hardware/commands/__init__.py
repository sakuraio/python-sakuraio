from .common import *
from .transmit import *
from .receive import *
from .file import *
from .operation import *

# Response
CMD_ERROR_NONE = 0x01
CMD_ERROR_PARITY = 0x02
CMD_ERROR_MISSING = 0x03
CMD_ERROR_INVALID_SYNTAX = 0x04
CMD_ERROR_RUNTIME = 0x05
CMD_ERROR_LOCKED = 0x06
CMD_ERROR_BUSY = 0x07


class CommandMixins(CommonMixins, TransmitMixins, ReceiveMixins, OperationMixins, FileMixins):
    pass
