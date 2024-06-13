from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/pricing')
def pricing():
    return render_template("pricing.html")

@app.route('/checkout')
def checkout():
    return render_template("checkout.html")

@app.route('/signup-pricing')
def signup_pricing():
    return render_template("signup_pricing.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)