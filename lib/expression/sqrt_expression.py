from .function_expression import FunctionExpression

class SqrtExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "sqrt")
