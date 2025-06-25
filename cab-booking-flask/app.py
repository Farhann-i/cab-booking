
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    pickup = db.Column(db.String(255))
    drop = db.Column(db.String(255))
    distance = db.Column(db.Float)
    fare = db.Column(db.Float)
    booking_time = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        pickup = request.form['pickup']
        drop = request.form['drop']
        distance = 10
        fare = distance * 15
        new_booking = Booking(name=name, phone=phone, pickup=pickup, drop=drop, distance=distance, fare=fare)
        db.session.add(new_booking)
        db.session.commit()
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=10000)
