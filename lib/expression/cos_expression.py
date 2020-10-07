from .function_expression import FunctionExpression

class CosExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "cos")
