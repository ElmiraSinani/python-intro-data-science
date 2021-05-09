class InvalidInputError(Exception):
    def __init__(self, msg, val):
        self.msg = msg
        self.val = val

    def __repr__(self):
        print(self.msg, ": ", str(self.val))
