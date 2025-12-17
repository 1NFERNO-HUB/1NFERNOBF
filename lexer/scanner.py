# lexer/stream.py
class Stream:
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.col = 1

    def peek(self, n=0):
        """Look at the character ahead without moving the pointer."""
        if self.pos + n >= len(self.source): return None
        return self.source[self.pos + n]

    def consume(self):
        """Read the current character and move the pointer forward."""
        char = self.peek()
        if char == "\n":
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        self.pos += 1
        return char

    def is_eof(self):
        return self.pos >= len(self.source)
