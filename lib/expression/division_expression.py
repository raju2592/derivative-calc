from .binary_expression import BinaryExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.subtraction_expression as subexpr
import lib.expression.variable_expression as varexpr
import lib.expression.constant_expression as constexpr
import lib.expression.power_expression as powexpr
import lib.expression.multiplication_expression as multiexpr
import lib.expression.derivative_expression as derivexpr


class DivisionExpression(BinaryExpression):
  def __init__(self, left_arg, right_arg):
    super().__init__(left_arg, right_arg, "/", precedence=3)

  def const_divider_derivative(self):
    rule = "d/dx cf(x) = c d/dx f(x)"
    child_derivative = self.left_arg.get_derivative()
    derivative = multiexpr.MultiplicationExpression(
      DivisionExpression(constexpr.ConstantExpression("1"), self.right_arg),
      child_derivative.result
    )
    rule_application = multiexpr.MultiplicationExpression(
      DivisionExpression(constexpr.ConstantExpression("1"), self.right_arg),
      derivexpr.DerivativeExpression(self.left_arg)
    )
    return Derivative(
      self,
      derivative,
      rule_application,
      [rule],
      [child_derivative]
    )

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    if self.right_arg.is_constant(): return self.const_divider_derivative()

    rule = "d/dx f(x)/g(x) = (g(x) d/dx f(x) - f(x) d/dx g(x))/(g(x))^2"
    
    left_derivative = self.left_arg.get_derivative()
    right_derivative = self.right_arg.get_derivative()

    result = DivisionExpression( 
      subexpr.SubtractionExpression(
        multiexpr.MultiplicationExpression(self.right_arg, left_derivative.result),
        multiexpr.MultiplicationExpression(self.left_arg, right_derivative.result)
      ),
      powexpr.PowerExpression(self.right_arg, constexpr.ConstantExpression("2"))
    )

    rule_application = DivisionExpression( 
      subexpr.SubtractionExpression(
        multiexpr.MultiplicationExpression(
          self.right_arg, derivexpr.DerivativeExpression(self.left_arg)
        ),
        multiexpr.MultiplicationExpression(
          self.left_arg, derivexpr.DerivativeExpression(self.right_arg)
        )
      ),
      powexpr.PowerExpression(self.right_arg, constexpr.ConstantExpression("2"))
    )

    return Derivative(
      self,
      result,
      rule_application,
      [rule],
      [left_derivative, right_derivative],
    )
  
  def simplify(self):
    left_arg = self.left_arg.simplify()
    right_arg = self.right_arg.simplify()

    left_val = None
    right_val = None

    if isinstance(left_arg, constexpr.ConstantExpression) and not left_arg.is_e():
      left_val = left_arg.get_value()
    
    if isinstance(right_arg, constexpr.ConstantExpression) and not right_arg.is_e():
      right_val = right_arg.get_value()

    if left_val == 0:
      return constexpr.ConstantExpression("0")
    
    if (left_val is not None and right_val is not None
      and right_val != 0 and left_val % right_val == 0):
      return constexpr.ConstantExpression(str(left_val // right_val))
    
    if right_val == 1: return left_arg
    
    if left_arg == right_arg: return constexpr.ConstantExpression("1")
    return DivisionExpression(left_arg, right_arg)
