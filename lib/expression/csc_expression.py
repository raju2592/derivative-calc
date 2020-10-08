from .function_expression import FunctionExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.negative_expression as negexpr
import lib.expression.multiplication_expression as multiexpr
import lib.expression.sin_expression as sinexpr
import lib.expression.variable_expression as varexpr
import lib.expression.cot_expression as cotexpr


class CscExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "csc")

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    csc_rule = "d/dx csc(x) = -csc(x)*cot(x)"

    derivative = multiexpr.MultiplicationExpression(
      negexpr.NegativeExpression(
        CscExpression(self.arg)
      ), cotexpr.CotExpression(self.arg)
    )

    if self.arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        derivative,
        [csc_rule],
        None
      )
    
    return utils.apply_chain_rule(self, csc_rule, derivative)
