from .expression import Expression
from ..derivative.derivative import Derivative
from .derivative_expression import DerivativeExpression
from .constant_expression import ConstantExpression

class VariableExpression(Expression):
  def __init__(self):
    super().__init__(precedence=0)

  def is_constant(self):
    return False


  def __eq__(self, value):
    return isinstance(value, VariableExpression)
