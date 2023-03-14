from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit/<int:marks>')       # this will allow you to enter a number in this url and get output accordingly
def submit(marks):
    return render_template('output.html',variable=marks)


@app.route('/checkfor')
def checkfor():
    diction={'name':'Amit','Age':26}
    return render_template('checkfor.html',variable=diction)


@app.route('/check',methods=['POST','GET'])
def check():
    if request.method=='POST':
        maths = float(request.form['maths'])        # maths is given inside 'name' tag in html file 
        science = float(request.form['science'])
        total_score = maths+science
    
    return redirect(url_for('submit',marks=total_score))

    

if __name__=='__main__':
    app.run(debug=True)