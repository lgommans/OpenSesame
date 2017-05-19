# Python 3.x
class OpenSesame:
    def __init__(self, filename):
        # According to [1], binary-files are read in buffered mode by default,
        # where the buffer size is determined by the underlying block size.
        # [1] https://docs.python.org/3.6/library/functions.html#open
        self.file_handle = open(filename, "rb")

        if not self.file_handle.seekable():
            # For speed reasons. When we found our desired boundary, we rewind
            # using seek() and copy the whole block at once.
            raise Exception("Input must be seekable!")

    def int(self):
        """ Read the next word and return it as an int """
        return int(self.word())

    def integer(self):
        return self.int()

    def number(self):
        """ Read the next word and return it as a number (decimal) """
        return float(self.word())

    def float(self):
        return self.number()

    def double(self):
        return self.number()

    def num(self):
        return self.number()

    def bytes(self, length):
        """ Read N bytes """
        return self.file_handle.read(length)

    def read(self, length):
        return self.bytes(length)

    def raw(self, length):
        return self.bytes(length)

    def word(self):
        """ Read until the next whitespace (newline, space, tab) """
        word = self.readUntil([b"\r\n", b"\n", b"\r", b" ", b"\t"])

        if word[-1] == "\r":
            return word

        return word

    def string(self):
        return self.word()

    def line(self):
        """ Read the next line (until \r\n, \n or \r, whichever comes first) """
        line = self.readUntil([b"\r\n", b"\n", b"\r"])

        if line[-1] == "\r":
            return line

        return line
        
    def readline(self):
        return self.line()

    def readUntil(self, until_list):
        """ Read until one of the characters in until_list is encountered.

            It will ignore any leading characters that are in until_list,
            e.g. if the file contains "    one " and you read until " " (space),
            it will return "one".
        """

        if type(until_list) != list:
            raise Exception("Until_list is not a list.")

        # We read bytes, so our until_list must be bytes
        for i, c in enumerate(until_list): # index, character
            if type(c) != bytes:
                until_list[i] = bytes(c, "UTF-8")

        # We don't want to get stuck on EOF
        until_list.append(b"")

        read_length = 0
        while read_length == 0:
            while self.file_handle.read(1) not in until_list:
                read_length += 1

        if self.file_handle.read(1) == b"":
            # EOF. Seek back and return until EOF
            self.file_handle.seek(-read_length, 1)
            return self.file_handle.read()

        # From 3.1 onwards, the constant SEEK_CUR exists. But for backwards
        # compatibility, let's hardcode 1.
        self.file_handle.seek(-read_length - 2, 1)

        return self.file_handle.read(read_length)

