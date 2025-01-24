from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
  """
  This function handles the calculation logic and renders the calculator template.
  """
  error = None
  result = ''
  if request.method == 'POST':
    try:
      expression = request.form['expression']
      result = eval(expression)
    except SyntaxError as e:
      error = f"Invalid expression: {str(e)}"
  return render_template('calculator.html', result=result, error=error)

if __name__ == '__main__':
  app.run(debug=True)
