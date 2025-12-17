# lexer/scanner.py
from .stream import Stream

class Scanner:
    KEYWORDS = {"local", "function", "if", "then", "else", "end", "return", "true", "false", "nil"}
    
    def __init__(self, source):
        self.stream = Stream(source)
        self.tokens = []

    def tokenize(self):
        while not self.stream.is_eof():
            char = self.stream.peek()

            if char.isspace():
                self.stream.consume()
            elif char.isalpha() or char == "_":
                self.read_identifier()
            elif char.isdigit():
                self.read_number()
            elif char == '"' or char == "'":
                self.read_string(char)
            elif char == "-":
                # Check for comments
                if self.stream.peek(1) == "-":
                    self.skip_comment()
                else:
                    self.add_token("OPERATOR", self.stream.consume())
            else:
                self.add_token("SYMBOL", self.stream.consume())
        
        return self.tokens

    def read_identifier(self):
        content = ""
        while not self.stream.is_eof() and (self.stream.peek().isalnum() or self.stream.peek() == "_"):
            content += self.stream.consume()
        
        token_type = "KEYWORD" if content in self.KEYWORDS else "IDENTIFIER"
        self.add_token(token_type, content)

    def add_token(self, type, value):
        self.tokens.append({"type": type, "value": value, "line": self.stream.line})
