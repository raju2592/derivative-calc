from .expression import Expression

class UnaryExpression(Expression):
  def __init__(self, arg, operator, precedence):
    super().__init__(precedence)
    self.arg = arg
    self.operator = operator

  def is_constant(self):
    return self.arg.is_constant()

  def __eq__(self, value):
    return type(self) is type(value) and value.arg == self.arg
