
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Dummy secret for security-scanner practice only
API_KEY = "DEMO_KEY_NOT_REAL_12345"

@app.route("/")
def home():
    return """
    <h1>DevSecOps Security Lab</h1>
    <p>Welcome to our test application!</p>
    <form action="/greet" method="GET">
        <input name="name" placeholder="Enter your name">
        <button type="submit">Submit</button>
    </form>
    """

@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return render_template_string("<h2>Hello, " + name + "!</h2>")

if __name__ == "__main__":
    app.run(debug=True)
