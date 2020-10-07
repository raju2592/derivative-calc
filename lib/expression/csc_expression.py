from .function_expression import FunctionExpression

class CscExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "csc")
