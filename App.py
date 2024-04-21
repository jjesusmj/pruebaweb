from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        valor_a = float(request.form['valor_a'])
        valor_b = float(request.form['valor_b'])
        resultado = valor_a + valor_b
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
