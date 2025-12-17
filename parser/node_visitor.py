# parser/node_visitor.py

class NodeVisitor:
    """The base traveler that walks the 1NFERNO AST."""
    
    def visit(self, node):
        """Dynamic dispatcher: calls visit_NodeName based on the node type."""
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Fallback: If no specific visit method exists, visit all children."""
        for field, value in vars(node).items():
            if isinstance(value, list):
                for item in value:
                    if hasattr(item, '__dict__'): self.visit(item)
            elif hasattr(value, '__dict__'):
                self.visit(value)

    # Example visitor methods (you will override these in your transformers)
    def visit_LocalAssign(self, node):
        self.generic_visit(node)

    def visit_BinaryOp(self, node):
        self.generic_visit(node)
