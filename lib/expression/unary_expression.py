from .expression import Expression
import lib.expression.binary_expression as binexpr

class UnaryExpression(Expression):
  def __init__(self, arg, operator, precedence):
    super().__init__(precedence)
    self.arg = arg
    self.operator = operator

  def is_constant(self):
    return self.arg.is_constant()

  def to_asciimath(self):
    if (isinstance(self.arg, binexpr.BinaryExpression) 
      and self.arg.precedence > self.precedence):
      return self.operator + "(" + self.arg.to_asciimath() + ")"
    
    return self.operator + self.arg.to_asciimath()

  def __eq__(self, value):
    return type(self) is type(value) and value.arg == self.arg
