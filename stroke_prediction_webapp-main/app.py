# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:52:20 2022

@author: SREERAM S
"""

from flask import Flask, request, render_template, flash, jsonify
import pickle


app = Flask(__name__)
app.secret_key = "apkofriowjfkf"

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/output",methods=["POST","GET"])


#user-input
def output():
    if request.method == 'POST':
        
        #gender
        g = request.form['gender'].lower()
        if g == "male":
            g = 1
        elif g == "female":
            g = 0
        else:
            g = 2
            
        #age
        a = int(request.form['age'])
        a = ((a-0.08)/(82-0.08))
        
        
        #hyper-tension
        hyt = request.form['hypertension'].lower
        if hyt == "yes":
            hyt = 1
        else:
            hyt = 0
            
        
        #heart-disease
        ht = request.form['heart-disease'].lower()
        if ht == "yes":
            ht = 1
        else:
            ht = 0
            
        
        #marriage
        m = request.form['marriage'].lower()
        if m == "yes":
            m = 1
        else:
            m = 0
            
        
        #worktype
        w = request.form['worktype'].lower()
        if w == "government":
            w = 0
        elif w == "student":
            w = 1
        elif w == "private":
            w = 2
        elif w == "self-employed":
            w = 3
        else:
            w = 4
            
            
        #residency-type
        r = request.form['residency'].lower()
        if r == "urban":
            r = 1
        else:
            r = 0
            
        #glucose-levels
        gl = int(request.form['glucose'])
        gl =  ((int(gl) - 55)/(271 - 55))
            
            
        #bmi
        b = int(request.form['bmi'])
        b = ((b-10.3)/(97.6-10.3))
        
            
        #smoking
        s = request.form['smoking'].lower()
        if s == "unknown":
            s = 0
        elif s == "never smoked":
            s = 1
        elif s == "formerly smoked":
            s = 2
        elif s == "smokes":
            s = 3
        else:
            s = 0

        try:
            prediction = stroke_pred(g,a,hyt,ht,m,w,r,gl,b,s)
            return render_template('index.html',prediction=prediction)

        except ValueError:
            return "Please Enter Valid Values"
        

#prediction-model
def stroke_pred(g,a,hyt,ht,m,w,r,gl,b,s):
    
    #load model
    model = pickle.load(open('model.pkl','rb'))

    #predictions
    result = model.predict([[g,a,hyt,ht,m,w,r,gl,b,s]])

    #output
    if result[0] == 1:
        pred = 'Person has chances of Having Stroke'
    else:
        pred = 'Person has no risk of Stroke'

    return pred

if __name__ == "__main__":
    app.run(debug=True)

