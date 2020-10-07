from .binary_expression import BinaryExpression
from ..derivative.derivative import Derivative

class SubtractionExpression(BinaryExpression):
  def __init__(self, left_arg, right_arg):
    super().__init__(left_arg, right_arg, "-", precedence=5)


  def get_derivative(self):
    pass
