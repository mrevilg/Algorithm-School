# AST Walkthrough

import ast

class ReplaceBinOp(ast.NodeTransformer):
    """Replace operation by addition in binary operation"""
    def visit_BinOp(self, node):
        return ast.BinOp(left=node.lefty, op=ast.Add(), right=node.right)

tree = ast.parse("x = 1/3")
ast.fix_missing_locations(tree)