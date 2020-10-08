from lib.expression.expressions import *

def test_multiplication_derivative():
  expr = MultiplicationExpression(VariableExpression(), ConstantExpression("2"))
  derivative = expr.get_derivative()
  assert derivative.result == MultiplicationExpression(
    ConstantExpression("2"), ConstantExpression("1")
  )

  expr = MultiplicationExpression(ConstantExpression("2"), VariableExpression())
  derivative = expr.get_derivative()
  assert derivative.result == MultiplicationExpression(
    ConstantExpression("2"), ConstantExpression("1")
  )

  expr = MultiplicationExpression(VariableExpression(), VariableExpression())
  derivative = expr.get_derivative()
  assert derivative.result == AdditionExpression(
    MultiplicationExpression(
      VariableExpression(), ConstantExpression("1")
    ),
    MultiplicationExpression(
      VariableExpression(), ConstantExpression("1")
    )
  )

