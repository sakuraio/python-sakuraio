class SakuraIOClientBaseExceptions(ValueError):
    pass


class UnSupportedExceptions(SakuraIOClientBaseExceptions):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return '[ERROR] {0} is unsupported {1} option.'.format(self.value, self.type)
