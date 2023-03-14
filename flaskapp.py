from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit/<int:marks>')       # this will allow you to enter a number in this url and get output accordingly
def submit(marks):
    if marks>50:
        return redirect(url_for('success',score=marks)) # redirect to pass page, observe that function name is passed not url(pass)
    else:
        return redirect(url_for('fail',score=marks))    # this will redirect to fail page
    

@app.route('/pass/<int:score>')
def success(score):
    return f"According to your score:{score} you have passed"

@app.route('/fail/<int:score>')
def fail(score):
    return f"According to your score:{score} you have failed"

@app.route('/check',methods=['POST','GET'])
def check():
    if request.method=='POST':
        maths = float(request.form['maths'])        # maths is given inside 'name' tag in html file 
        science = float(request.form['science'])
        total_score = maths+science
    
    return redirect(url_for('submit',marks=total_score))

    

if __name__=='__main__':
    app.run(debug=True)