from lib.expression.expressions import *

def test_cos_derivative():
  expr = CosExpression(VariableExpression())
  derivative = expr.get_derivative()
  assert derivative.result == NegativeExpression(SinExpression(VariableExpression()))

  expr = CosExpression(ConstantExpression("2"))
  derivative = expr.get_derivative()
  assert derivative.result == ConstantExpression("0")

  expr = CosExpression(AdditionExpression(
    VariableExpression(), VariableExpression()
  ))
  derivative = expr.get_derivative()
  assert derivative.result == MultiplicationExpression(
    NegativeExpression(
      SinExpression(AdditionExpression(
        VariableExpression(), VariableExpression()
      ))
    ),
    AdditionExpression(ConstantExpression("1"), ConstantExpression("1"))
  )


def test_to_asciimath():
  expr = CosExpression(VariableExpression())
  math_str = expr.to_asciimath()
  assert math_str == "cos(x)"

  expr = CosExpression(ConstantExpression("90"))
  math_str = expr.to_asciimath()
  assert math_str == "cos(90)"