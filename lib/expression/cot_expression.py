from .function_expression import FunctionExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.negative_expression as negexpr
import lib.expression.sin_expression as sinexpr
import lib.expression.variable_expression as varexpr
import lib.expression.constant_expression as constexpr
import lib.expression.power_expression as powexpr
import lib.expression.csc_expression as cscexpr

class CotExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "cot")
  
  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    cot_rule = "d/dx cot(x) = -csc^2(x)"

    derivative = negexpr.NegativeExpression(
      powexpr.PowerExpression(
        cscexpr.CscExpression(self.arg), constexpr.ConstantExpression(2)
      )
    )

    if self.arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        derivative,
        [cot_rule],
        None
      )
    
    return utils.apply_chain_rule(self, cot_rule, derivative)
