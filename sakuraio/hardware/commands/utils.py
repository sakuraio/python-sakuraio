import struct
import platform

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
        result += value
        return result
    else:
        TypeError()

def value_to_bytes(value):
    """Convert value to raw values.

    :param value:
        Value to Convert
    :type value: integer, float, str or bytes

    :return: Tuple of `Type` string and `Value` list
    :rtype: (str, list)
    """

    if isinstance(value, float):
        return ("d", pack("<d", value))

    if isinstance(value, int):
        if value > 9223372036854775807:
            return ("L", pack("<Q", value))
        return ("l", pack("<q", value))

    if platform.python_version_tuple()[0] == "2" and isinstance(value, long):
        return ("L", pack("<Q", value))

    if isinstance(value, str):
        if platform.python_version_tuple()[0] == "2":
            result = []
            for c in value.encode("utf-8"):
                result.append(ord(c))
            return ("b", (result+[0x00]*8)[:8])
        else:
            return ("b", (list(value.encode("utf-8"))+[0x00]*8)[:8])

    if isinstance(value, bytes):
        return ("b", (list(value)+[0x00]*8)[:8])

    raise ValueError("Unsupported Type %s", value.__class__)
