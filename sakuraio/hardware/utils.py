import struct


def pack(fmt, *args):
    """pack() is wrapper of struct.pack
    """

    value = struct.pack(fmt, *args)
    result = []

    if isinstance(value, str):
        # For Python2
        for v in value:
            result.append(ord(v))

        return result
    elif isinstance(value, bytes):
        # For Python3
        return value
    else:
        TypeError()
