from .function_expression import FunctionExpression

class SinExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "sin")
