from .unary_expression import UnaryExpression

class NegativeExpression(UnaryExpression):
  def __init__(self, arg):
    super().__init__(arg, "-", 2)
