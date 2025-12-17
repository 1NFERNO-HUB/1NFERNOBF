# lexer/tokens.py
from enum import Enum, auto

class TokenType(Enum):
    # --- Special ---
    EOF = auto()          # End of File
    IDENTIFIER = auto()   # Variable/Function names
    NUMBER = auto()       # 1, 1.5, 0xFF
    STRING = auto()       # "Hello", 'World', [[Multiline]]
    
    # --- Keywords ---
    LOCAL = auto()
    FUNCTION = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    ELSEIF = auto()
    END = auto()
    WHILE = auto()
    REPEAT = auto()
    UNTIL = auto()
    FOR = auto()
    DO = auto()
    IN = auto()
    RETURN = auto()
    BREAK = auto()
    TRUE = auto()
    FALSE = auto()
    NIL = auto()

    # --- Operators & Symbols ---
    PLUS = auto()      # +
    MINUS = auto()     # -
    MUL = auto()       # *
    DIV = auto()       # /
    MOD = auto()       # %
    POW = auto()       # ^
    LEN = auto()       # #
    EQ = auto()        # ==
    NEQ = auto()       # ~=
    LT = auto()        # <
    GT = auto()        # >
    LTE = auto()       # <=
    GTE = auto()       # >=
    ASSIGN = auto()    # =
    LPAREN = auto()    # (
    RPAREN = auto()    # )
    LBRACKET = auto()  # [
    RBRACKET = auto()  # ]
    LBRACE = auto()    # {
    RBRACE = auto()    # }
    COMMA = auto()     # ,
    DOT = auto()       # .
    COLON = auto()     # :
    CONCAT = auto()    # ..
    VARARG = auto()    # ...

class Token:
    def __init__(self, type: TokenType, value: any, line: int, col: int):
        self.type = type
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f"Token({self.type.name}, '{self.value}', line={self.line})"
