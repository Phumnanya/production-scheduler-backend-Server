from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import text
from flask_cors import CORS  # to allow React access

app = Flask(__name__)
CORS(app)  # enable CORS for React

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eustace:Menezman6860@localhost/production_scheduler'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model (table)
class database(db.Model):
    __tablename__ = 'production_orders' # Explicitly name the table
    id = db.Column(db.Integer, primary_key=True)
    machine = db.Column(db.String(50))
    date = db.Column(db.Date, nullable=False)
    task = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    startTime = db.Column(db.String(10))
    endTime = db.Column(db.String(10))

# Create tables
with app.app_context():
    db.create_all()

# get orders from db Route
@app.route("/orders", methods=["GET"])
def get_orders():
    orders = database.query.all()
    output = []
    print(f"DEBUG: Found {len(orders)} orders in the database.")
    for o in orders:
        output.append({
            "id": o.id, 
            "machine": o.machine,
            "task": o.task,
            "quantity": o.quantity,
            "date": str(o.date), 
            "startTime": o.startTime,
            "endTime": o.endTime
        })
    return jsonify(output)

#add new orders route
@app.route("/orders", methods=["POST"])
def add_order():
    data = request.get_json()
    new_order = database(machine=data["machine"], date=data["date"], task=data["task"], 
                     quantity=data["quantity"], startTime=data["startTime"], endTime=data["endTime"])
    db.session.add(new_order)
    db.session.commit()
    success = True
    if success:
        return jsonify({"message": "Order booked Successfully!",
                        "redirect_url": "/dashboard"}), 201

#check collision route
@app.route('/check-collision', methods=['POST'])
def check_collision():
    data = request.json
    machine = data.get('machine')
    order_date = data.get('date')      # e.g., '2026-02-19'
    new_start = data.get('startTime')     # e.g., '10:00'
    new_end = data.get('endTime')         # e.g., '11:00'
    
    # Combining date and time for comparison with PostgreSQL 'NOW()'
    # This checks if the requested time range overlaps with any ACTIVE (not elapsed) order
    query = text("""
        SELECT id FROM production_orders 
            WHERE machine = :machine 
              AND date = :order_date
              AND (:new_start < "endTime" AND :new_end > "startTime")
    """)

    result = db.session.execute(query, {
        'machine': machine,
        'order_date': order_date,
        'new_start': new_start,
        'new_end': new_end
    }).fetchone()
    
    # If result is not None, a conflict exists
    if result:
        return jsonify({"conflict": True, "message": "Time slot is already taken"}), 200
    
    return jsonify({"conflict": False}), 200

#delete order route
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = database.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
        
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
