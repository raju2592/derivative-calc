from lib.lexer import tokenize
from lib.token import Token

def test_tokenize():
  r = tokenize("a")
  assert r.success == False

  r = tokenize("x + 2 * x * y")
  assert r.success == False

  r = tokenize("x")
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == "x"
  assert r.tokens[0].lexeme == "x"
  
  r = tokenize("1.23") 
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == "number"
  assert r.tokens[0].lexeme == "1.23"

  r = tokenize("+") 
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == "+"
  assert r.tokens[0].lexeme == "+"

  r = tokenize("-") 
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == "-"
  assert r.tokens[0].lexeme == "-"

  r = tokenize("*") 
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == "*"
  assert r.tokens[0].lexeme == "*"

  r = tokenize("/") 
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == "/"
  assert r.tokens[0].lexeme == "/"

  r = tokenize("^") 
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == "^"
  assert r.tokens[0].lexeme == "^"

  r = tokenize("(") 
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == "("
  assert r.tokens[0].lexeme == "("

  r = tokenize(")") 
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == ")"
  assert r.tokens[0].lexeme == ")"

  r = tokenize("  ") 
  assert r.success == True
  assert len(r.tokens) == 1
  assert r.tokens[0].name == "whitespace"
  assert r.tokens[0].lexeme == "  "

  r = tokenize("()") 
  assert r.success == True
  assert len(r.tokens) == 2
  assert r.tokens[0].name == "("
  assert r.tokens[0].lexeme == "("
  assert r.tokens[1].name == ")"
  assert r.tokens[1].lexeme == ")"

  r = tokenize("x+1") 
  assert r.success == True
  assert len(r.tokens) == 3
  assert r.tokens[0].name == "x"
  assert r.tokens[0].lexeme == "x"
  assert r.tokens[1].name == "+"
  assert r.tokens[1].lexeme == "+"
  assert r.tokens[2].name == "number"
  assert r.tokens[2].lexeme == "1"

  r = tokenize("x+1") 
  assert r.success == True
  assert len(r.tokens) == 3
  assert r.tokens[0].name == "x"
  assert r.tokens[0].lexeme == "x"
  assert r.tokens[1].name == "+"
  assert r.tokens[1].lexeme == "+"
  assert r.tokens[2].name == "number"
  assert r.tokens[2].lexeme == "1"

  r = tokenize("12.3  +x") 
  assert r.success == True
  assert len(r.tokens) == 4
  assert r.tokens[0].name == "number"
  assert r.tokens[0].lexeme == "12.3"
  assert r.tokens[1].name == "whitespace"
  assert r.tokens[1].lexeme == "  "
  assert r.tokens[2].name == "+"
  assert r.tokens[2].lexeme == "+"
  assert r.tokens[3].name == "x"
  assert r.tokens[3].lexeme == "x"
