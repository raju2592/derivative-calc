from .unary_expression import UnaryExpression
import lib.expression.negative_expression as negexpr

class DerivativeExpression(UnaryExpression):
  def __init__(self, arg):
    super().__init__(arg, "d/dx", 4)

  def to_asciimath(self):
    if isinstance(self.arg, negexpr.NegativeExpression):
      return self.operator + "(" + self.arg.to_asciimath() + ")"
    return super().to_asciimath()
