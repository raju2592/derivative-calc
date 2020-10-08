from .derivative import Derivative

import lib.expression.constant_expression as ce
import lib.expression.multiplication_expression as me
import lib.expression.derivative_expression as de

def constant_derivative(expression):
  return Derivative(
    expression,
    ce.ConstantExpression("0"),
    ce.ConstantExpression("0"),
    ['d/dx c = 0'],
    None
  )

def apply_chain_rule(expression, rule, u_derivative, child = None):
  chain_rule = "dy/dx = dy/(du)(du)/dx"

  if child is None:
    child = expression.arg
  child_derivative = child.get_derivative()

  return Derivative(
    expression,
    me.MultiplicationExpression(u_derivative, child_derivative.result),
    me.MultiplicationExpression(u_derivative, de.DerivativeExpression(child)),
    [rule, chain_rule],
    [child_derivative]
  )
