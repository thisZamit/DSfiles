from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/check')
def hello():
    return "<h1> Welcome bro <h1>"

@app.route('/about')
def about():
    return "You've entered the about page"

if __name__=='__main__':
    app.run(debug=True)