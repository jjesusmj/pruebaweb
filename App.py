from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        valor_a = request.form.get("valor_a")
        valor_b = request.form.get("valor_b")
        resultado = int(valor_a) + int(valor_b)
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
