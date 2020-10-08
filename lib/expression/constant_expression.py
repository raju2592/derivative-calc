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

  def is_int(self):
    try: 
      int(self.value)
      return True
    except ValueError:
      return False

  def get_value(self):
    if self.is_e(): return 2.71828
    if self.is_int: return int(self.value)
    return float(self.value)
  
  def to_asciimath(self):
    return self.value
  
  def __eq__(self, value):
    return (isinstance(value, ConstantExpression)
      and value.value == self.value)
