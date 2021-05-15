from flask import Flask,render_template,redirect,request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('rfc_model.pkl')



@app.route("/")
def home():
    return render_template('home.html')


@app.route('/prediction',methods=['GET','POST'])
def intro():
    if request.method=="POST":
        return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=="POST":
        age = int(request.form['age'])
        jobtype = int(request.form['job-type'])
        marital = int(request.form['marital'])
        education = int(request.form['education'])
        balance = int(request.form['balance'])
        housing = int(request.form['housing'])
        loan = int(request.form['personal loan'])
        contact = int(request.form['contact'])
        day = int(request.form['day'])
        month = int(request.form['month'])
        duration = int(request.form['duration'])
        campaign = int(request.form['campaign'])
        previous = int(request.form['previous'])
        poutcome = int(request.form['poutcome'])

        cols = [age,jobtype,marital,education,balance,housing,loan,contact,day,month,duration,campaign,previous,
                poutcome]
        cols = np.array(cols)
        cols = cols.reshape(1, 14)

        prediction = model.predict(cols)[0]
        print(prediction)
        if(prediction==1):
            return render_template("positive.html")
        if(prediction==0):
            return render_template("negative.html")

        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)