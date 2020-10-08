from ..derivative.derivative import Derivative
from .expression import Expression
import lib.derivative.derivative_utils as utils

class ConstantExpression(Expression):
  def __init__(self, value):
    super().__init__(precedence=0)
    self.value = value

  def is_constant(self):
    return True

  def get_derivative(self):
    return utils.constant_derivative(self)

  def is_e(self):
    return self.value == "e"

  def get_value(self):
    pass
  
  def to_asciimath(self):
    return self.value
  
  def __eq__(self, value):
    return (isinstance(value, ConstantExpression)
      and value.value == self.value)
