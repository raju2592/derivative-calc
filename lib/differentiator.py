from .lexer.lexer import tokenize
from .parser.parser import get_expression
from .expression.derivative_expression import DerivativeExpression
import random

def add_quote(str):
  return "`" + str + "`"

class Result:
  def __init__(self, success, answer = None, story = None):
    self.success = success
    self.answer = answer
    self.story = story

def get_story(derivative):
  random.seed()
  starting_text = [
    'We know that, ',
    'It is the case that, ',
    'Remember that, ',
  ][random.randint(0, 2)]

  more_starting_text = [
    'We also know that, ',
    'It is also the case that, ',
    'Also, Remember that, ',
  ][random.randint(0, 2)]
  
  story = []
  applied_rules = derivative.applied_rules
  story.append(starting_text + add_quote(applied_rules[0]))

  if len(applied_rules) > 1:
    story.append(more_starting_text + add_quote(applied_rules[1]))

  derivative_expression = DerivativeExpression(derivative.arg)
  rule_application = derivative.rule_application

  story.append("So, " + 
    add_quote(derivative_expression.to_asciimath() + " = " 
      + rule_application.to_asciimath()
    )
  )

  answer = add_quote(derivative_expression.to_asciimath() + " = " + derivative.result.to_asciimath()) + "."

  if derivative.child_derivatives is not None:
    child_derivatives = derivative.child_derivatives
    if (len(child_derivatives) == 2 
      and child_derivatives[0].arg == child_derivatives[1].arg):
      child_derivatives = child_derivatives[0:1]

    for child_derivative in child_derivatives:
      story.extend(get_story(child_derivative).story)

    ending_texts = []
    if len(derivative.applied_rules) == 2:
      ending_texts = [
        "So, by the rules, " + add_quote(derivative.applied_rules[0]) + ","
        + " and " + add_quote(derivative.applied_rules[1]) + ","        
      ]
    else:
      ending_texts = [
        "So, by the rule, " + add_quote(derivative.applied_rules[0]) + ","
      ]

    ending_texts.append(answer)
    story.extend(ending_texts)

  return Result(True, answer, story)
  
def differentiate(str):
  tokenizationResult = tokenize(str)
  if not tokenizationResult.success: return Result(False)

  tokens = list(filter(lambda token: token.name != "whitespace", tokenizationResult.tokens))

  expression = get_expression(tokens)
  if expression is None: return Result(False)

  derivative = expression.get_derivative()
  return get_story(derivative)
