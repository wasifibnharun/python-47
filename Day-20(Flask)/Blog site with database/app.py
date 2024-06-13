from flask import Flask,render_template,redirect,request
import sqlite3

app = Flask(__name__)

# connect = sqlite3.connect('flaskapp.db')
# connect.execute('CREATE TABLE IF NOT EXISTS articles(id INTEGER AUTO_INCREMENT)')

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/articles')
def articles():
    #connect to db
    db = sqlite3.connect('posts.db')
    cursor = db.cursor()
    
    #Get data from db
    cursor.execute('SELECT * FROM posts ORDER BY id DESC')
    posts = cursor.fetchall()

    #close db connection
    db.close()

    return render_template("articles.html", posts = posts)

if (__name__) == '__main__':
    app.run(debug=True)