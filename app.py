from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    income = float(request.form.get("income", 0))
    expenses = float(request.form.get("expenses", 0))
    savings = income - expenses

    if savings > 0:
        recommendation = "You should invest your savings."
    else:
        recommendation = "Consider reducing your expenses."

    return render_template("index.html", 
                           income=income, 
                           expenses=expenses, 
                           savings=savings, 
                           recommendation=recommendation)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
