from .function_expression import FunctionExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.cos_expression as cosexpr
import lib.expression.multiplication_expression as multiexpr
import lib.expression.variable_expression as varexpr

class SinExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "sin")

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    sin_rule = "d/dx sin(x) = cos(x)"

    derivative = cosexpr.CosExpression(self.arg)
  
    if self.arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        None,
        [sin_rule],
        None
      )

    return utils.apply_chain_rule(self, sin_rule, derivative)

  def simplify(self):
    return SinExpression(self.arg.simplify())