from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/check')
def hello():
    return "hello"
@app.route('/about')
def about():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)