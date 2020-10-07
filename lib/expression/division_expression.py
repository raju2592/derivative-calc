from .binary_expression import BinaryExpression
from ..derivative.derivative import Derivative

class DivisionExpression(BinaryExpression):
  def __init__(self, left_arg, right_arg):
    super().__init__(left_arg, right_arg, "/", precedence=3)

  def get_derivative(self):
    pass
