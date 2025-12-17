class Node:
    """Base class for all AST nodes."""
    pass

class Statement(Node): pass
class Expression(Node): pass

class Block(Node):
    def __init__(self, body):
        self.body = body # A list of Statements

class LocalAssign(Statement):
    def __init__(self, targets, values):
        self.targets = targets # Names like 'x', 'y'
        self.values = values   # Values like 10, 20

class BinaryOp(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op # +, -, *, etc.
        self.right = right
