from flask import Flask, render_template, response, request
import time
import threading

app = Flask(__name__, template_folder = "app/templates")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False, port = 4000)
