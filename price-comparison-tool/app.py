from flask import Flask, render_template, request, jsonify
from scraper import get_prices

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/compare")
def compare():
    product = request.args.get("product")
    results = get_prices(product)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)