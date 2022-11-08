from flask import Flask
from controllers.product import product

app = Flask(__name__)

app.register_blueprint(product, url_prefix='/products')

@app.route("/")
def hello():
    return "Hello, World!!"

if __name__ == "__main__":
    app.run(debug=True)