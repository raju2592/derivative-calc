from .grammar import start_symbol
from .grammar import TERMINAL, NON_TERMINAL

class Match:
  def __init__(self, symbol, rule, expression, submatches, start, end):
    self.symbol = symbol
    self.rule = rule
    self.expression = expression
    self.submatches = submatches
    self.start = start
    self.end = end

def match_rule(tokens, symbol, rule, pos):
  production = rule.production

  length = len(tokens)
  submatches = []
  cur_pos = pos

  for child_symbol in production:
    match = parse_symbol(tokens, child_symbol, cur_pos)
    if match is None:
      return None
    submatches.append(match)
    cur_pos = match.end
  
  expression = None
  if rule.expression_builder is not None:
    expression = rule.expression_builder(submatches)
  
  return Match(symbol, rule, expression, submatches, pos, cur_pos)

def match_terminal(tokens, symbol, pos):
  if symbol.symbol_name == "_epsilon":
    return Match(symbol, None, None, None, pos, pos)
  if pos == len(tokens): return None
  if symbol.symbol_name == tokens[pos].name:
    return Match(symbol, None, tokens[pos].lexeme, None, pos, pos + 1)

  return None

def parse_symbol(tokens, symbol, pos):
  if symbol.symbol_type == TERMINAL: return match_terminal(tokens, symbol, pos)

  symbol_rules = symbol.prod_rules
  for rule in symbol_rules:
    match = match_rule(tokens, symbol, rule, pos)
    if match is not None: return match
  
  return None

def get_expression(tokens):
  match = parse_symbol(tokens, start_symbol, 0)
  if match is None: return None
  if match.end < len(tokens): return None
  return match.expression
