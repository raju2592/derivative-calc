class Expression:
  def __init__(self, precedence):
    self.precedence = precedence

  def is_constant(self):
    pass

  def get_derivative(self):
    pass

  def to_asciimath(self):
    pass

  def simplify(self):
    return self;
