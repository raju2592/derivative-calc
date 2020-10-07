from .expression_builders import *

class Rule:
  def __init__(self, production, expression_builder):
    self.production = production
    self.expression_builder = expression_builder


TERMINAL = 0
NON_TERMINAL = 1

class Symbol:
  def __init__(self, symbol_name, symbol_type, prod_rules = None):
    self.symbol_name = symbol_name
    self.symbol_type = symbol_type
    self.prod_rules = []
    if prod_rules is not None: self.prod_rules = prod_rules

  def add_rule(self, production, expression_builder):
    self.prod_rules.append(Rule(production, expression_builder))



expression = Symbol("expression", NON_TERMINAL)
variable = Symbol("variable", NON_TERMINAL)
constant = Symbol("contant", NON_TERMINAL)
x = Symbol("x", TERMINAL)
number = Symbol("number", TERMINAL)
e = Symbol("e", TERMINAL)
sin = Symbol("sin", TERMINAL)
sin_expr = Symbol("sin_expr", NON_TERMINAL)
cos = Symbol("cos", TERMINAL)
cos_expr = Symbol("cos_expr", NON_TERMINAL)
tan = Symbol("tan", TERMINAL)
tan_expr = Symbol("tan_expr", NON_TERMINAL)
cot = Symbol("cot", TERMINAL)
cot_expr = Symbol("cot_expr", NON_TERMINAL)
sec = Symbol("sec", TERMINAL)
sec_expr = Symbol("sec_expr", NON_TERMINAL)
csc = Symbol("csc", TERMINAL)
csc_expr = Symbol("csc_expr", NON_TERMINAL)
ln = Symbol("ln", TERMINAL)
ln_expr = Symbol("ln_expr", NON_TERMINAL)
sqrt = Symbol("sqrt", TERMINAL)
sqrt_expr = Symbol("sqrt_expr", NON_TERMINAL)
power = Symbol("^", TERMINAL)
plus = Symbol("+", TERMINAL)
minus = Symbol("-", TERMINAL)
plus = Symbol("+", TERMINAL)
multiplication = Symbol("*", TERMINAL)
division = Symbol("/", TERMINAL)
brace_open = Symbol("(", TERMINAL)
brace_close = Symbol(")", TERMINAL)
epsilon = Symbol("_epsilon", TERMINAL)
atom = Symbol("atom", NON_TERMINAL)
unary_plus_expr = Symbol("unary_plus_expr", NON_TERMINAL)
unary_minus_expr = Symbol("unary_minus_expr", NON_TERMINAL)
unary_expr = Symbol("unary_expr", NON_TERMINAL)
power_expr = Symbol("power", NON_TERMINAL)
unary_plus_power_expr = Symbol("unary_plus_power_expr", NON_TERMINAL)
unary_minus_power_expr = Symbol("unary_minus_power_expr", NON_TERMINAL)
factor = Symbol("factor", NON_TERMINAL)
more_factors = Symbol("more_factors", NON_TERMINAL)
term = Symbol("term", NON_TERMINAL)
more_terms = Symbol("more_terms", NON_TERMINAL)

variable.add_rule([x], make_variable)

constant.add_rule([number], make_constant)
constant.add_rule([e], make_constant)

sin_expr.add_rule([sin, brace_open, expression, brace_close], make_sin)

cos_expr.add_rule([cos, brace_open, expression, brace_close], make_cos)

tan_expr.add_rule([tan, brace_open, expression, brace_close], make_tan)

cot_expr.add_rule([cot, brace_open, expression, brace_close], make_cot)

sec_expr.add_rule([sec, brace_open, expression, brace_close], make_sec)

csc_expr.add_rule([csc, brace_open, expression, brace_close], make_csc)

ln_expr.add_rule([ln, brace_open, expression, brace_close], make_ln)

sqrt_expr.add_rule([sqrt, brace_open, expression, brace_close], make_sqrt)

atom.add_rule([variable], return_child)
atom.add_rule([constant], return_child)
atom.add_rule([sin_expr], return_child)
atom.add_rule([cos_expr], return_child)
atom.add_rule([tan_expr], return_child)
atom.add_rule([cot_expr], return_child)
atom.add_rule([sec_expr], return_child)
atom.add_rule([csc_expr], return_child)
atom.add_rule([ln_expr], return_child)
atom.add_rule([sqrt_expr], return_child)
atom.add_rule([brace_open, expression, brace_close], return_child)

power_expr.add_rule([atom, power, power_expr], make_power)
power_expr.add_rule([atom, power, unary_expr], make_power)
power_expr.add_rule([atom, power, atom], make_power)

unary_plus_expr.add_rule([plus, power_expr], remove_unary_plus)
unary_plus_expr.add_rule([plus, unary_expr], remove_unary_plus)
unary_plus_expr.add_rule([plus, atom], remove_unary_plus)

unary_minus_expr.add_rule([minus, power_expr], make_negative)
unary_minus_expr.add_rule([minus, unary_expr], make_negative)
unary_minus_expr.add_rule([minus, atom], make_negative)

unary_expr.add_rule([unary_plus_expr], return_child)
unary_expr.add_rule([unary_minus_expr], return_child)

factor.add_rule([unary_expr], return_child)
factor.add_rule([power_expr], return_child)
factor.add_rule([atom], return_child)

term.add_rule([factor, more_factors], make_term)

more_factors.add_rule([multiplication, factor, more_factors], None)
more_factors.add_rule([division, factor, more_factors], None)
more_factors.add_rule([epsilon], None)

expression.add_rule([term, more_terms], make_expression)

more_terms.add_rule([plus, term, more_terms], None)
more_terms.add_rule([minus, term, more_terms], None)
more_terms.add_rule([epsilon], None)

start_symbol = expression
