from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # to allow React access

app = Flask(__name__)
CORS(app)  # enable CORS for React

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eustace:Menezman6860@localhost/production_scheduler'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model (table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine = db.Column(db.String(50))
    task = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    startTime = db.Column(db.String(10))
    endTime = db.Column(db.String(10))
    #email = db.Column(db.String(120), unique=True)

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route("/orders", methods=["GET"])
def get_orders():
    orders = User.query.all()
    return jsonify([{"id": o.id, "machine": o.machine, "task": o.task,
                     "quantity": o.quantity, "startTime": o.startTime, "endTime": o.endTime} 
                    for o in orders])

@app.route("/orders", methods=["POST"])
def add_order():
    data = request.get_json()
    new_order = User(machine=data["machine"], task=data["task"], quantity=data["quantity"],
                     startTime=data["startTime"], endTime=data["endTime"])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order added!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
