from lib.expression.expressions import *

def test_division_derivative():
  expr = DivisionExpression(VariableExpression(), ConstantExpression("2"))
  derivative = expr.get_derivative()
  assert derivative.result == MultiplicationExpression(
    DivisionExpression(ConstantExpression("1"), ConstantExpression("2")),
    ConstantExpression("1")
  )

  expr = DivisionExpression(VariableExpression(), VariableExpression())
  derivative = expr.get_derivative()
  assert derivative.result == DivisionExpression(
    SubtractionExpression(
      MultiplicationExpression(
        VariableExpression(), ConstantExpression("1")
      ),
      MultiplicationExpression(
        VariableExpression(), ConstantExpression("1")
      )
    ),
    PowerExpression(VariableExpression(), ConstantExpression("2"))
  )
