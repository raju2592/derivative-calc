class Derivative:
  def __init__(self, arg, result, rule_application, applied_rules, child_derivatives):
    self.arg = arg
    self.result = result.simplify()
    self.unsimplified_result = result
    self.applied_rules = applied_rules
    self.rule_application = rule_application
    self.child_derivatives = child_derivatives
