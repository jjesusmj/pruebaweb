from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        valor_a = request.form.get("valor_a")
        valor_b = request.form.get("valor_b")
        # Aquí puedes hacer la suma y devolver el resultado
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
