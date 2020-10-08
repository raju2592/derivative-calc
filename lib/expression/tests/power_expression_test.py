from lib.expression.expressions import *

def test_multiplication_derivative():
  expr = PowerExpression(VariableExpression(), ConstantExpression("3"))
  derivative = expr.get_derivative()
  assert derivative.unsimplified_result == MultiplicationExpression(
    ConstantExpression("3"),
    PowerExpression(
      VariableExpression(),
      SubtractionExpression(ConstantExpression("3"), ConstantExpression("1"))
    )
  )

  expr = PowerExpression(SinExpression(VariableExpression()), ConstantExpression("3"))
  derivative = expr.get_derivative()
  assert derivative.unsimplified_result == MultiplicationExpression(
    MultiplicationExpression(
      ConstantExpression("3"),
      PowerExpression(
        SinExpression(VariableExpression()),
        SubtractionExpression(ConstantExpression("3"), ConstantExpression("1"))
      )
    ),
    CosExpression(VariableExpression())
  )
  