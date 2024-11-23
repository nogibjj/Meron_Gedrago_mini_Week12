from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template
template = """
<!doctype html>
<html>
    <body>
        <h1>Prime Number Checker</h1>
        <form action="/" method="post">
            <input type="number" name="number" placeholder="Enter a number" required>
            <button type="submit">Check</button>
        </form>
        {% if result is not none %}
        <h2>Result:</h2>
        <p>{{ result }}</p>
        {% endif %}
    </body>
</html>
"""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            number = int(request.form.get("number"))
            if is_prime(number):
                result = f"{number} is a prime number."
            else:
                result = f"{number} is not a prime number."
        except ValueError:
            result = "Invalid input. Please enter a valid number."
    return render_template_string(template, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
