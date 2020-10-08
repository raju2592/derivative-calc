from .expression import Expression
from ..derivative.derivative import Derivative
from .derivative_expression import DerivativeExpression
import lib.expression.constant_expression as constexpr

class VariableExpression(Expression):
  def __init__(self):
    super().__init__(precedence=0)

  def is_constant(self):
    return False

  def get_derivative(self):
    return Derivative(
      self,
      constexpr.ConstantExpression("1"),
      constexpr.ConstantExpression("1"),
      ["d/dx x = 1"],
      None
    )


  def __eq__(self, value):
    return isinstance(value, VariableExpression)
