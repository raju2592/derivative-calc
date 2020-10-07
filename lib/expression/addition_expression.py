from .binary_expression import BinaryExpression
from .variable_expression import VariableExpression
from ..derivative.derivative import Derivative

class AdditionExpression(BinaryExpression):
  def __init__(self, left_arg, right_arg):
    super().__init__(left_arg, right_arg, "+", precedence=4)

  def get_derivative(self):
    pass


  def get_value(self):
    pass
