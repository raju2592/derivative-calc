from lib.differentiator import differentiate
from lib.expression.expressions import *

def test_differntiate():
  derivative_result = differentiate("x")
  assert derivative_result.answer == "1"

  derivative_result = differentiate("x + 1")
  assert derivative_result.answer == "1+0"