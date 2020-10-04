import re
from .token import Token

class TokenizationResult:
  def __init__(self):
    self.success = True
    self.tokens = []
  
  def add_token(self, token):
    self.tokens.append(token)
  
  def set_failure(self):
      self.success = False


config = {
  "whitespace": r"\s+",
  "number": r"([0-9]*[.])?[0-9]+",
  "e": "e",
  "x": "x",
  "e": "e",
  "x": "x",
  "sin": "sin",
  "cos": "cos",
  "tan": "tan",
  "cot": "cot",
  "sec": "sec",
  "csc": "csc",
  "ln": "ln",
  "sqrt": "sqrt",
  "+": r"\+",
  "-": r"\-",
  "*": r"\*",
  "/": "/",
  "(": r"\(",
  ")": r"\)",
  "^": r"\^"
}

patterns = {}

for name in config:
  pattern = config[name]
  patterns[name] = re.compile(pattern)


def get_token(str, pos):
  match_len = 0
  name = ""
  for n in patterns:
    regex = patterns[n]
    m = regex.match(str, pos)
    if m is not None:
      start = m.start()
      end = m.end()
      l = end - start
      if l > match_len:
        match_len, name = l, n
  return (match_len, name) 


def tokenize(str):
  length = len(str)
  pos = 0
  result = TokenizationResult()

  while pos < length:
    match_len, token_name = get_token(str, pos)
    if match_len == 0:
      result.set_failure()
      return result
    print(match_len, token_name)
    lexeme = str[pos:pos + match_len]
    pos = pos + match_len
    result.add_token(Token(token_name, lexeme))
  
  return result
