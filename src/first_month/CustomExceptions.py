class InvalidInputError(Exception):
    def __init__(self, msg, val):
        self.msg = msg
        self.val = val

    def __repr__(self):
        return repr(self.msg)
