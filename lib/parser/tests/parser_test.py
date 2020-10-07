from lib.parser.parser import get_expression
from lib.expression.expressions import *
from lib.lexer.token_class import Token

def t(s):
  return Token(s, s)

def n(s):
  return Token("number", s)

def test_parse_x():
  tokens = [t("x")]
  expr = get_expression(tokens)
  assert expr == VariableExpression()

def test_parse_constant():
  tokens = [n("123")]
  expr = get_expression(tokens)
  assert expr == ConstantExpression("123")

  tokens = [Token("e", "e")]
  expr = get_expression(tokens)
  assert expr == ConstantExpression("e")

def test_parse_multiplication():
  tokens = [n("123"), t("*"), t("x")]
  expr = get_expression(tokens)
  assert expr == MultiplicationExpression(
    ConstantExpression("123"), VariableExpression()
  )

  tokens = [t("x"), t("*"), t("x"), t("*"), t("x")]
  expr = get_expression(tokens)
  assert expr == MultiplicationExpression(MultiplicationExpression(
    VariableExpression(), VariableExpression()
  ), VariableExpression())

def test_parse_division():
  tokens = [n("123"), t("/"), t("x")]
  expr = get_expression(tokens)
  assert expr == DivisionExpression(
    ConstantExpression("123"), VariableExpression()
  )

def test_parse_term():
  tokens = [n("123"), t("/"), t("x"), t("*"), t("e")]
  expr = get_expression(tokens)
  assert expr == MultiplicationExpression(DivisionExpression(
    ConstantExpression("123"), VariableExpression()
  ), ConstantExpression("e"))

def test_parse_power():
  tokens = [n("123"), t("^"), t("x")]
  expr = get_expression(tokens)
  assert expr == PowerExpression(
    ConstantExpression("123"), VariableExpression()
  )

  tokens = [t("x"), t("^"), t("-"), t("x")]
  expr = get_expression(tokens)
  assert expr == PowerExpression(
    VariableExpression(), NegativeExpression(VariableExpression())
  )

  tokens = [t("x"), t("^"), t("-"), t("x"), t("^"), t("x")]
  expr = get_expression(tokens)
  assert expr == PowerExpression(
    VariableExpression(), NegativeExpression(
      PowerExpression(VariableExpression(), VariableExpression())
    )
  )

def test_unary_positive():
  tokens = [t("+"), t("x")]
  expr = get_expression(tokens)
  assert expr == VariableExpression()

  tokens = [t("+"), t("x"), t("^"), t("x")]
  expr = get_expression(tokens)
  assert expr == PowerExpression(
    VariableExpression(), VariableExpression()
  )

def test_negative():
  tokens = [t("-"), t("x")]
  expr = get_expression(tokens)
  assert expr == NegativeExpression(VariableExpression())

  tokens = [t("-"), t("x"), t("^"), t("x")]
  expr = get_expression(tokens)
  assert expr == NegativeExpression(PowerExpression(
    VariableExpression(), VariableExpression()
  ))

  tokens = [t("-"), t("-"), t("x")]
  expr = get_expression(tokens)
  assert expr == NegativeExpression(NegativeExpression(
    VariableExpression()
  ))

def test_addition():
  tokens = [t("x"), t("+"), n("1")]
  expr = get_expression(tokens)
  assert expr == AdditionExpression(VariableExpression(), ConstantExpression("1"))

  tokens = [t("x"), t("+"), t("-"), n("1")]
  expr = get_expression(tokens)
  assert expr == AdditionExpression(VariableExpression(),
    NegativeExpression(ConstantExpression("1")))

  tokens = [t("x"), t("+"), t("x"), t("+"), t("x")]
  expr = get_expression(tokens)
  assert expr == AdditionExpression(AdditionExpression(
    VariableExpression(), VariableExpression()
  ), VariableExpression())

  tokens = [t("x"), t("+"), t("-"), n("2"), t("^"), t("-"), t("x"), t("*"), t("x")]
  expr = get_expression(tokens)
  assert expr == AdditionExpression(VariableExpression(),
    MultiplicationExpression(NegativeExpression(
      PowerExpression(
        ConstantExpression("2"), NegativeExpression(VariableExpression())
      )
    ), VariableExpression())
  )

def test_subtraction():
  tokens = [t("x"), t("-"), n("1")]
  expr = get_expression(tokens)
  assert expr == SubtractionExpression(VariableExpression(), ConstantExpression("1"))

  tokens = [t("x"), t("-"), t("-"), n("1")]
  expr = get_expression(tokens)
  assert expr == SubtractionExpression(VariableExpression(),
    NegativeExpression(ConstantExpression("1")))

  tokens = [t("x"), t("-"), t("x"), t("-"), t("x")]
  expr = get_expression(tokens)
  assert expr == SubtractionExpression(SubtractionExpression(
    VariableExpression(), VariableExpression()
  ), VariableExpression())

  tokens = [t("x"), t("-"), t("-"), n("2"), t("^"), t("-"), t("x"), t("*"), t("x")]
  expr = get_expression(tokens)
  assert expr == SubtractionExpression(VariableExpression(),
    MultiplicationExpression(NegativeExpression(
      PowerExpression(
        ConstantExpression("2"), NegativeExpression(VariableExpression())
      )
    ), VariableExpression())
  )

def test_sin():
  tokens = [t("sin"), t("("), t("x"), t(")")]
  expr = get_expression(tokens)
  assert expr == SinExpression(VariableExpression())

  tokens = [t("sin"), t("("), t("x"), t("+"), t("x"), t(")")]
  expr = get_expression(tokens)
  assert expr == SinExpression(AdditionExpression(
    VariableExpression(), VariableExpression()
  ))

def test_cos():
  tokens = [t("cos"), t("("), t("x"), t(")")]
  expr = get_expression(tokens)
  assert expr == CosExpression(VariableExpression())

  tokens = [t("cos"), t("("), t("x"), t("+"), t("x"), t(")")]
  expr = get_expression(tokens)
  assert expr == CosExpression(AdditionExpression(
    VariableExpression(), VariableExpression()
  ))
