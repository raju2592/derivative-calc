import random
from urllib.parse import unquote
from flask import Flask, render_template, request, jsonify
from lib.differentiator import differentiate

app = Flask(__name__)

@app.route('/', methods = ['get'])
def hello_world():
  random.seed()
  input = [
    '(1 + sin(x)) ^ 3',
    'ln(sqrt(x) + 1)',
    '10 * (x + tan(x))'
  ][(random.randint(0, 2))]
  return render_template("main.html", input=input)


@app.route('/getDerivative', methods = ['get'])
def get_derivative():
  input = unquote(request.args.get('function'))
  result = differentiate(input)
  return jsonify(result.__dict__)

if __name__ == "__main__":
  app.run()
