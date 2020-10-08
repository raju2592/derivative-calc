from .function_expression import FunctionExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.negative_expression as negexpr
import lib.expression.sin_expression as sinexpr
import lib.expression.variable_expression as varexpr

class CosExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "cos")

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    cos_rule = "d/dx cos(x) = - sin(x)"
    derivative = negexpr.NegativeExpression(sinexpr.SinExpression(self.arg))

    if self.arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        derivative,
        [cos_rule],
        None
      )
    
    return utils.apply_chain_rule(self, cos_rule, derivative)
