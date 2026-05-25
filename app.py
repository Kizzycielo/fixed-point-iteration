from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Fixed-Point Function
# g(x) = cos(x)

def g(x):
    return math.cos(x)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    steps = []

    if request.method == "POST":

        x0 = float(request.form["x0"])
        tolerance = float(request.form["tolerance"])
        max_iterations = int(request.form["max_iterations"])

        x_old = x0

        for i in range(max_iterations):

            x_new = g(x_old)

            error = abs(x_new - x_old)

            steps.append({
                "iteration": i + 1,
                "x_old": round(x_old, 6),
                "x_new": round(x_new, 6),
                "error": round(error, 6)
            })

            # STOP CONDITION
            if error < tolerance:
                result = round(x_new, 6)
                break

            x_old = x_new

        # if no convergence
        if result is None:
            result = round(x_new, 6)

    return render_template(
        "index.html",
        result=result,
        steps=steps
    )


if __name__ == "__main__":
    app.run(debug=True)