from .binary_expression import BinaryExpression
from ..derivative.derivative import Derivative

class MultiplicationExpression(BinaryExpression):
  def __init__(self, left_arg, right_arg):
    super().__init__(left_arg, right_arg, "*", precedence=3)

  def is_constant(self):
    return self.left_arg.is_constant() and self.right_arg.is_constant()

  def get_derivative(self):
    pass

