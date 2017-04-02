class SakuraIOBaseException(ValueError):
    pass


class CommandError(SakuraIOBaseException):

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "Invalid response status '0x{0:02x}'".format(self.status)


class ParityError(SakuraIOBaseException):

    def __init__(self):
        pass

    def __str__(self):
        return "Invalid parity"
