# AST Walkthrough

import ast

class ReplaceBinOp(ast.NodeTransformer):
    """Replace operation by addition in binary operation"""