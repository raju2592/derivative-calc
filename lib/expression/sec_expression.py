from .function_expression import FunctionExpression

class SecExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "sec")
