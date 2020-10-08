from .binary_expression import BinaryExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.derivative_expression as derivexpr
import lib.expression.addition_expression as addexpr
import lib.expression.derivative_expression as derivexpr
import lib.expression.constant_expression as constexpr

class MultiplicationExpression(BinaryExpression):
  def __init__(self, left_arg, right_arg):
    super().__init__(left_arg, right_arg, "*", precedence=3)

  def is_constant(self):
    return self.left_arg.is_constant() and self.right_arg.is_constant()

  def const_arg_derivative(self, const_arg, other_arg):
    rule = "d/dx cf(x) = c d/dx f(x)"
    child_derivative = other_arg.get_derivative()
    derivative = MultiplicationExpression(const_arg, child_derivative.result)
  
    return Derivative(
      self,
      derivative,
      MultiplicationExpression(const_arg, derivexpr.DerivativeExpression(other_arg)),
      [rule],
      [child_derivative]
    )

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    if self.left_arg.is_constant(): return self.const_arg_derivative(self.left_arg, self.right_arg)
    if self.right_arg.is_constant(): return self.const_arg_derivative(self.right_arg, self.left_arg)

    multiplication_rule = "d/dx f(x)g(x) = f(x) d/dx g(x) + g(x) d/dx f(x)"

    left_derivative = self.left_arg.get_derivative()
    right_derivative = self.right_arg.get_derivative()

    result = addexpr.AdditionExpression(
      MultiplicationExpression(self.left_arg, right_derivative.result),
      MultiplicationExpression(self.right_arg, left_derivative.result)
    )

    rule_application = addexpr.AdditionExpression(
      MultiplicationExpression(self.left_arg, derivexpr.DerivativeExpression(self.right_arg)),
      MultiplicationExpression(self.right_arg, derivexpr.DerivativeExpression(self.left_arg))
    )

    return Derivative(
      self,
      result,
      rule_application,
      [multiplication_rule],
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
  
    if left_val == 0 or right_val == 0:
      return constexpr.ConstantExpression("0")
    
    if left_val is not None and right_val is not None:
      return constexpr.ConstantExpression(str(left_val * right_val))

    if left_val == 1: return right_arg
    if right_val == 1: return left_arg

    return MultiplicationExpression(left_arg, right_arg)
