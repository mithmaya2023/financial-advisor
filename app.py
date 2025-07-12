from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    income = float(request.form.get("income", 0))
    expenses = float(request.form.get("expenses", 0))
    debt = float(request.form.get("debt", 0))
    goal = float(request.form.get("goal", 0))

    savings = income - expenses
    savings_rate = (savings / income * 100) if income > 0 else 0

    # Dynamic recommendation logic
    if savings <= 0:
        recommendation = "Consider reducing your expenses."
    elif debt > 0:
        recommendation = "Focus on paying off your debt first."
    elif goal > 0 and savings < goal:
        recommendation = f"Increase your savings to reach your goal of {goal}."
    else:
        recommendation = "Great job! You can consider investing your savings."

    return render_template(
        "index.html",
        income=income,
        expenses=expenses,
        debt=debt,
        goal=goal,
        savings=savings,
        savings_rate=savings_rate,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
