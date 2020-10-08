from .function_expression import FunctionExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.division_expression as divexpr
import lib.expression.multiplication_expression as multiexpr
import lib.expression.variable_expression as varexpr
import lib.expression.constant_expression as constexpr

class SqrtExpression(FunctionExpression):
  def __init__(self, arg):
    super().__init__(arg, "sqrt")

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    sqrt_rule = "d/dx sqrt(x) = 1/(2*sqrt(x))"

    derivative = divexpr.DivisionExpression(
      constexpr.ConstantExpression("1"),
      multiexpr.MultiplicationExpression(constexpr.ConstantExpression("2"), self)
    )

    if self.arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        derivative,
        [sqrt_rule],
        None
      )
    
    return utils.apply_chain_rule(self, sqrt_rule, derivative)
