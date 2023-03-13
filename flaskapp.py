from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)

# nothing in home page

@app.route('/submit/<int:marks>')       # this will allow you to enter a number in this url and get output accordingly
def hello(marks):
    if marks>50:
        return redirect(url_for('success',score=marks)) # redirect to pass page, observe that function name is passed not url(pass)
    else:
        return redirect(url_for('fail',score=marks))    # this will redirect to fail page
    

@app.route('/pass/<int:score>')
def success(score):
    return f"According to score you entered:{score} you have passed"

@app.route('/fail/<int:score>')
def fail(score):
    return f"According to score you entered:{score} you have failed"




    

if __name__=='__main__':
    app.run(debug=True)