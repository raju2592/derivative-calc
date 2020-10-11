from .unary_expression import UnaryExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.derivative_expression as derivexpr
import lib.expression.constant_expression as constexpr

class NegativeExpression(UnaryExpression):
  def __init__(self, arg):
    super().__init__(arg, "-", 2)

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    neg_rule = "d/dx (-f(x)) = - d/dx f(x)"
    child_derivative = self.arg.get_derivative()
    derivative = NegativeExpression(child_derivative.result)
  
    return Derivative(
      self,
      derivative,
      NegativeExpression(derivexpr.DerivativeExpression(self.arg)),
      [neg_rule],
      [child_derivative]
    )

  def simplify(self):
    arg = self.arg.simplify()

    if isinstance(arg, constexpr.ConstantExpression) and not arg.is_e():
      val = arg.get_value()
      if val == 0: return constexpr.ConstantExpression("0")
      return constexpr.ConstantExpression(str(-1 * val))
    
    if isinstance(arg, NegativeExpression): return arg.arg
    return NegativeExpression(arg)
