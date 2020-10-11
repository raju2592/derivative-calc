from .binary_expression import BinaryExpression
from ..derivative.derivative import Derivative
import lib.derivative.derivative_utils as utils
import lib.expression.subtraction_expression as subexpr
import lib.expression.addition_expression as addexpr
import lib.expression.variable_expression as varexpr
import lib.expression.constant_expression as constexpr
import lib.expression.power_expression as powexpr
import lib.expression.multiplication_expression as multiexpr
import lib.expression.division_expression as divexpr
import lib.expression.derivative_expression as derivexpr
import lib.expression.ln_expression as lnexpr
import lib.expression.negative_expression as negexpr

class PowerExpression(BinaryExpression):
  def __init__(self, left_arg, right_arg):
    super().__init__(left_arg, right_arg, "^", precedence=1)

  def is_constant(self):
    if self.left_arg.is_constant() and self.right_arg.is_constant():
      return True
    return self.right_arg == constexpr.ConstantExpression("0")

  def const_power_derivative(self):
    rule = "d/dx x^n = n*x^(n-1)"

    derivative = multiexpr.MultiplicationExpression(
      self.right_arg,
      PowerExpression(
        self.left_arg,
        subexpr.SubtractionExpression(self.right_arg, constexpr.ConstantExpression("1"))
      )
    )

    if self.left_arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        derivative,
        [rule],
        None
      )
    
    return utils.apply_chain_rule(self, rule, derivative, self.left_arg)

  def const_base_derivative(self):
    derivative = None
    rule = None

    rule_application = None
    if isinstance(self.left_arg, constexpr.ConstantExpression) and self.left_arg.is_e():
      derivative = self
      rule = "d/dx e^x = e^x"
    else:
      derivative = multiexpr.MultiplicationExpression(self, lnexpr.LnExpression(self.left_arg))
      rule = "d/dx a^x = a^x * ln(a)"
      rule_application = derivative

    if self.right_arg == varexpr.VariableExpression():
      return Derivative(
        self,
        derivative,
        rule_application,
        [rule],
        None
      )
    
    return utils.apply_chain_rule(self, rule, derivative, self.right_arg)
  
  def get_derivative(self):
    if self.is_constant(): return utils.constant_derivative(self)

    if self.right_arg.is_constant(): return self.const_power_derivative()
    if self.left_arg.is_constant(): return self.const_base_derivative()

    rule = "d/dx u ^ v = u ^ v * (ln (u) * d/dx v + (v * d/dx u)/ u)"
    
    left_derivative = self.left_arg.get_derivative()
    right_derivative = self.right_arg.get_derivative()

    result = multiexpr.MultiplicationExpression( 
      self,
      addexpr.AdditionExpression(
        multiexpr.MultiplicationExpression(lnexpr.LnExpression(self.left_arg), right_derivative.result),
        divexpr.DivisionExpression(
          multiexpr.MultiplicationExpression(self.right_arg, left_derivative.result), self.left_arg
        )
      )
    )

    rule_application = multiexpr.MultiplicationExpression( 
      self,
      addexpr.AdditionExpression(
        multiexpr.MultiplicationExpression(
          lnexpr.LnExpression(self.left_arg), derivexpr.DerivativeExpression(self.right_arg)
        ),
        divexpr.DivisionExpression(
          multiexpr.MultiplicationExpression(
            self.right_arg, derivexpr.DerivativeExpression(self.left_arg)
          ), self.left_arg
        )
      )
    )

    return Derivative(
      self,
      result,
      rule_application,
      [rule],
      [left_derivative, right_derivative],
    )
  
  def to_asciimath(self):
    left_str = self.left_arg.to_asciimath()
    if self.left_arg.precedence >= self.precedence:
      left_str = "(" + left_str + ")"
    right_str = "(" + self.right_arg.to_asciimath() + ")"
    return left_str + self.operator + right_str

  def simplify(self):
    left_arg = self.left_arg.simplify()
    right_arg = self.right_arg.simplify()
    
    if isinstance(right_arg, constexpr.ConstantExpression) and not right_arg.is_e():
      right_val = right_arg.get_value()
      if (right_val == 0): return constexpr.ConstantExpression("1")
      if (right_val == 1): return left_arg
    return PowerExpression(left_arg, right_arg)
