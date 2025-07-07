from flask import Flask, render_template, jsonify, url_for, redirect, request
import os

app = Flask(__name__, template_folder = "app/templates")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cam', methods=['POST'])
def TakePhoto():
    return url_for('index')

if __name__ == "__main__":
    app.run(debug=False, port = 4000)
