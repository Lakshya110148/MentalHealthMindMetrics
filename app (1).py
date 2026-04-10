from flask import Flask, render_template, request
from model import predict_stress, get_solutions, build_chart_data
import os

app = Flask(__name__)

# Simple in-memory history for demo purposes
history = []

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    solutions = []
    score = None
    chart_data = build_chart_data(history)

    if request.method == "POST":
        sleep = float(request.form["sleep"])
        screen = float(request.form["screen"])
        activity = float(request.form["activity"])
        typing = float(request.form["typing"])

        result, score = predict_stress(sleep, screen, activity, typing)
        solutions = get_solutions(result, sleep, screen, activity, typing)

        history.append({
            "sleep": sleep,
            "screen": screen,
            "activity": activity,
            "typing": typing,
            "stress": result,
            "score": score
        })

        chart_data = build_chart_data(history)

    return render_template(
        "index.html",
        result=result,
        solutions=solutions,
        score=score,
        chart_data=chart_data
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
