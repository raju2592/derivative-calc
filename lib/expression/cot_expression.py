from .function_expression import FunctionExpression

class CotExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "cot")
