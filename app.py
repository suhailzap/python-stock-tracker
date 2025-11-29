from flask import Flask

app = Flask(__name__)

@app.route("/")
def charge():
    return "Here are all of the available products"

@app.route("/price")
def price():
    return "Here are the current prices of products"

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False, host="0.0.0.0", port=5000)
