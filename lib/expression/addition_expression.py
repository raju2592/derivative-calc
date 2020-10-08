from .binary_expression import BinaryExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.derivative_expression as derivexpr

class AdditionExpression(BinaryExpression):
  def __init__(self, left_arg, right_arg):
    super().__init__(left_arg, right_arg, "+", precedence=5)

  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    left_derivative = self.left_arg.get_derivative()
    right_derivative = self.right_arg.get_derivative()

    rule_application = AdditionExpression(
      derivexpr.DerivativeExpression(self.left_arg),
      derivexpr.DerivativeExpression(self.right_arg)
    )

    applied_rules = ["d/dx (f(x) + g(x)) = d/dx f(x) + d/dx g(x)"]

    result = AdditionExpression(left_derivative.result, right_derivative.result)
    child_derivatives = [left_derivative, right_derivative]
  
    return Derivative(self, result, rule_application, applied_rules, child_derivatives)
  
  def to_asciimath(self):
    left_str = self.left_arg.to_asciimath()
    right_str = self.right_arg.to_asciimath()
    print(left_str, self.operator, right_str, self.right_arg.precedence, self.precedence)
    if self.left_arg.precedence >= self.precedence:
      left_str = "(" + left_str + ")"
    if (self.right_arg.precedence >= self.precedence
      and isinstance(self.right_arg, BinaryExpression)):
      right_str = "(" + right_str + ")"
    elif right_str[0] == "-":
      right_str = "(" + right_str + ")"
    return left_str + self.operator + right_str
