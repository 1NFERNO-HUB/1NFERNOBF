# parser/grammar.py
from .ast import *
from lexer.tokens import TokenType

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected_type=None):
        token = self.peek()
        if expected_type and token.type != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {token.type}")
        self.pos += 1
        return token

    def parse_chunk(self):
        """Entry point: Parses a whole Lua file into a Block."""
        statements = []
        while self.peek() and self.peek().type != TokenType.EOF:
            statements.append(self.parse_statement())
        return Block(statements)

    def parse_statement(self):
        token = self.peek()
        if token.type == TokenType.LOCAL:
            return self.parse_local()
        # Add logic for IF, WHILE, FUNCTION, etc.
        return self.parse_expression_statement()

    def parse_local(self):
        self.consume(TokenType.LOCAL)
        name = self.consume(TokenType.IDENTIFIER).value
        self.consume(TokenType.ASSIGN)
        value = self.parse_expression()
        return LocalAssign([name], [value])
