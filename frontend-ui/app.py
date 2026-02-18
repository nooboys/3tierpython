from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)

AUTH_URL = os.environ["AUTH_URL"]
BACKEND_URL = os.environ["BACKEND_URL"]

HTML = """
<h1>Task Manager</h1>
<form method="post">
Task: <input name="task">
<input type="submit">
</form>
<ul>
{% for t in tasks %}
<li>{{ t }}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    token = requests.post(f"{AUTH_URL}/login",
                          json={"username": "admin", "password": "admin"}).json()["token"]

    if request.method == "POST":
        task = request.form["task"]
        requests.post(f"{BACKEND_URL}/tasks/{task}")

    tasks = requests.get(f"{BACKEND_URL}/tasks").json()["tasks"]
    return render_template_string(HTML, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)