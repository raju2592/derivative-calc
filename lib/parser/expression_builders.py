from ..expression.expressions import *

def make_variable(submatches):
  return VariableExpression()

def make_constant(submatches):
  return ConstantExpression(submatches[0].expression)

def make_sin(submatches):
  return SinExpression(submatches[2].expression)

def make_cos(submatches):
  return CosExpression(submatches[2].expression)

def make_tan(submatches):
  return TanExpression(submatches[2].expression)

def make_cot(submatches):
  return CotExpression(submatches[2].expression)

def make_sec(submatches):
  return SecExpression(submatches[2].expression)

def make_csc(submatches):
  return CscExpression(submatches[2].expression)

def make_ln(submatches):
  return LnExpression(submatches[2].expression)

def make_sqrt(submatches):
  return SqrtExpression(submatches[2].expression)

def return_child(submatches):
  if len(submatches) == 1: return submatches[0].expression
  return submatches[1].expression

def make_power(submatches):
  return PowerExpression(submatches[0].expression, submatches[2].expression)

def remove_unary_plus(submatches):
  return submatches[1].expression

def make_negative(submatches):
  return NegativeExpression(submatches[1].expression)

def make_term(submatches):
  expr = submatches[0].expression
  more_factors_match = submatches[1]
  while len(more_factors_match.submatches) > 1:
    more_factors_child = more_factors_match.submatches
    operator = more_factors_child[0].symbol
    more_factor = more_factors_child[1].expression
    if operator.symbol_name == "*":
      expr = MultiplicationExpression(expr, more_factor)
    else:
      expr = DivisionExpression(expr, more_factor)
    more_factors_match = more_factors_child[2]
  
  return expr

def make_expression(submatches):
  expr = submatches[0].expression
  more_terms_match = submatches[1]
  while len(more_terms_match.submatches) > 1:
    more_terms_child = more_terms_match.submatches
    operator = more_terms_child[0].symbol
    more_term = more_terms_child[1].expression
    if operator.symbol_name == "+":
      expr = AdditionExpression(expr, more_term)
    else:
      expr = SubtractionExpression(expr, more_term)
    more_terms_match = more_terms_child[2]
  return expr
