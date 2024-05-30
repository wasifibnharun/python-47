from flask import Flask

app=Flask(__name__)

#creating a route
@app.route('/')
def index():
    return "Hello world"

@app.route('/about')
def about():
    return 'This is about page' 

@app.route('/product/<id>')
def product(id):
    return 'This is product page and you are viewing:'+str(id)

if __name__=='__main__':
    app.run(debug=True)