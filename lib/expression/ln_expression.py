from .function_expression import FunctionExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.variable_expression as varexpr
import lib.expression.constant_expression as constexpr
import lib.expression.division_expression as divexpr

class LnExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "ln")

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    ln_rule = "d/dx ln(x) = 1/x"

    derivative = divexpr.DivisionExpression(constexpr.ConstantExpression("1"), self.arg)

    if self.arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        derivative,
        [ln_rule],
        None
      )
    
    return utils.apply_chain_rule(self, ln_rule, derivative)