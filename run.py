import time
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, make_response, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pear.db'

db = SQLAlchemy(app)
products = []


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(35), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False, unique=True)

    def json(self):
        return {
            "title": self.title,
            "text": self.desc,
            "price": self.price,
            "image": self.image
        }


@app.route('/load')
def load():
    quantity = 3
    time.sleep(3)
    if request.args:
        counter = int(request.args.get('c'))
        print(counter)
        if counter == 0:
            res = make_response(jsonify(products[0:quantity]), 200)

        elif counter == len(products):
            res = make_response(jsonify({}), 200)

        else:
            res = make_response(jsonify(products[counter: counter + quantity]), 200)

        return res


@app.route("/")
def index():
    global products
    products = [i.json() for i in Product.query.all()]
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)

