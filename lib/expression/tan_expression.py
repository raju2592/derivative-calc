from .function_expression import FunctionExpression

class TanExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "tan")
