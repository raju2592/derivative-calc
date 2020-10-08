from lib.expression.addition_expression import AdditionExpression
from lib.expression.variable_expression import VariableExpression
from lib.expression.constant_expression import ConstantExpression

def test_addition_derivative():
  expr = AdditionExpression(VariableExpression(), VariableExpression())
  derivative = expr.get_derivative()
  assert derivative.result == AdditionExpression(
    ConstantExpression("1"), ConstantExpression("1")
  )

