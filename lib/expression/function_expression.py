from .expression import Expression

class FunctionExpression(Expression):
  def __init__(self, arg, function):
    super().__init__(precedence=0)
    self.arg = arg
    self.function = function

  def is_constant(self):
    return self.arg.is_constant()

  def to_asciimath(self):
    return self.function + "(" + self.arg.to_asciimath() + ")"

  def __eq__(self, value):
    return type(self) is type(value) and value.arg == self.arg
