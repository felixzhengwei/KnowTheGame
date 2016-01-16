from flask import Flask, render_template, request, jsonify
import json


app = Flask("know_the_game")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=3000, debug=True)
