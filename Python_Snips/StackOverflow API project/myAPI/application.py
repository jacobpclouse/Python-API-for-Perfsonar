from flask import Flask
app = Flask(__name__)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.na"

# https://youtu.be/qbLc5a9jdXo?t=2050

# routes
@app.route('/')
def index():
    return 'Welcome to CyberSpace!'

@app.route('/drinks')
def get_drinks():
    return {"drinks": "Drink data for right now!"}