from .unary_expression import UnaryExpression

class DerivativeExpression(UnaryExpression):
  def __init__(self, arg):
    super().__init__(arg, 4)
