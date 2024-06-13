from flask import Flask

app=Flask(__name__)

#creating a route
@app.route('/')
def index():
    return "<h4>Hello World</h4>"

if __name__=='__main__':
    app.run(debug=True)