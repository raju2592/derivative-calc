from .function_expression import FunctionExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.power_expression as powexpr
import lib.expression.sec_expression as secexpr
import lib.expression.multiplication_expression as multiexpr
import lib.expression.variable_expression as varexpr
import lib.expression.constant_expression as constexpr

class TanExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "tan")

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    tan_rule = "d/dx tan(x) = sec^2(x)"

    derivative = powexpr.PowerExpression(
      secexpr.SecExpression(self.arg), constexpr.ConstantExpression("2")
    )

    if self.arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        derivative,
        [tan_rule],
        None
      )
    
    return utils.apply_chain_rule(self, tan_rule, derivative)
