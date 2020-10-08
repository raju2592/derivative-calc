from lib.expression.expressions import *

def test_division_derivative():
  expr = DivisionExpression(VariableExpression(), ConstantExpression("2"))
  derivative = expr.get_derivative()
  assert derivative.unsimplified_result == MultiplicationExpression(
    DivisionExpression(ConstantExpression("1"), ConstantExpression("2")),
    ConstantExpression("1")
  )

  expr = DivisionExpression(VariableExpression(), VariableExpression())
  derivative = expr.get_derivative()
  assert derivative.unsimplified_result == DivisionExpression(
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

def test_simplify():
  expr = DivisionExpression(VariableExpression(), ConstantExpression("1"))
  assert expr.simplify() == VariableExpression()
