from .expression import Expression

class BinaryExpression(Expression):
  def __init__(self, left_arg, right_arg, operator, precedence):
    super().__init__(precedence)
    self.left_arg = left_arg
    self.right_arg = right_arg
    self.operator = operator

  def is_constant(self):
    return self.left_arg.is_constant() and self.right_arg.is_constant()

  def __eq__(self, value):
    return (type(self) is type(value) and value.left_arg == self.left_arg
      and value.right_arg == self.right_arg)
