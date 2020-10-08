from .function_expression import FunctionExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.tan_expression as tanexpr
import lib.expression.multiplication_expression as multiexpr
import lib.expression.variable_expression as varexpr

class SecExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "sec")

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    sec_rule = "d/dx sec(x) = sec(x)*tan(x)"

    derivative = multiexpr.MultiplicationExpression(
      SecExpression(self.arg), tanexpr.TanExpression(self.arg)
    )

    if self.arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        derivative,
        [sec_rule],
        None
      )
    
    return utils.apply_chain_rule(self, sec_rule, derivative)
  