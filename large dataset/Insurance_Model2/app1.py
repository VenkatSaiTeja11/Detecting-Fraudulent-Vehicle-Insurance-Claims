from flask import Flask,request, url_for, redirect, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("insurance_dd2.pkl", "rb"))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    text1 = request.form['1']
    text2 = request.form['2']
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text7 = request.form['7']
    text8 = request.form['8']
    text9 = request.form['9']
    text10 = request.form['10']
    text11 = request.form['11']
    text12 = request.form['12']
 
    row_df = pd.DataFrame([pd.Series([text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12])])
    print(row_df)
    prediction=model.predict_proba(row_df)
    output='{0:.{1}f}'.format(prediction[0][1], 2)
    output = str(float(output)*100)+'%'
    if output>str(0.5):
        return render_template('result.html',pred=f'Fraudulent. The Probability of fraudelent is {output}')
    else:
        return render_template('result.html',pred=f'Not fraudulent.\n Probability of fraudelent is {output}')

if __name__ == '__main__':
    app.run(debug=True)
