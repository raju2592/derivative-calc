from .expression import Expression

class BinaryExpression(Expression):
  def __init__(self, left_arg, right_arg, operator, precedence):
    super().__init__(precedence)
    self.left_arg = left_arg
    self.right_arg = right_arg
    self.operator = operator

  def is_constant(self):
    return self.left_arg.is_constant() and self.right_arg.is_constant()

  def to_asciimath(self):
    left_str = self.left_arg.to_asciimath()
    right_str = self.right_arg.to_asciimath()
    if self.left_arg.precedence > self.precedence:
       left_str = "(" + left_str + ")"
    if self.right_arg.precedence > self.precedence:
       right_str = "(" + right_str + ")"

    return left_str + self.operator + right_str

  def __eq__(self, value):
    return (type(self) is type(value) and value.left_arg == self.left_arg
      and value.right_arg == self.right_arg)
