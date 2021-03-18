from flask import Flask,render_template,redirect,request
import pandas as pd 
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

app=Flask(__name__)
model=joblib.load("model.pkl")
@app.route('/')
def index():
	return render_template("indix.html")

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':
        var1=float(request.form['preg'])
        var2=float(request.form['glucose'])
        var3=float(request.form['bldp'])
        var4=float(request.form['skinth'])
        var5=float(request.form['insulin'])
        var6=float(request.form['bmi'])
        var7=float(request.form['dpf'])
        var8=float(request.form['age'])
        varx=str(request.form['varr'])
        if varx=='germany':
            var9=1
            var10=0
        elif varx=='france':
            var9=0
            var10=1
        else:
            var9=0
            var10=0
        #var10=float(request.form['vare'])
        varyx=str(request.form['vary'])
        if varyx=='male':
            var11=1
        else:
            var11=0
        listofchurn=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11]
        listofchurn=np.array(listofchurn)
        listchurn=listofchurn.reshape(1,-1)
        listchurn=sc.fit_transform(listchurn)
        predictn=model.predict([listchurn])
        output=str(predictn)
        predictn=(predictn > 0.5)
        prediction=str(predictn)

    return render_template("indix.html", predicted=prediction[2],output=output)
if __name__== '__main__':
    app.run(debug=True)