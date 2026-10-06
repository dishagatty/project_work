from flask import Flask, request, render_template_string
from datetime import date

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Age Calculator</title>
</head>
<body>
    <h2>Age Calculator</h2>

    <form method="POST">
        <input type="date" name="dob" required>
        <button type="submit">Calculate Age</button>
    </form>

    {% if age %}
        <h3>Your age is {{ age }} years</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    age = None

    if request.method == "POST":
        dob = date.fromisoformat(request.form["dob"])
        today = date.today()

        age = today.year - dob.year

        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1

    return render_template_string(html, age=age)

if __name__ == "__main__":
    app.run(debug=True)