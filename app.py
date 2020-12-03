# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:36:55 2020

@author: admin
"""
import numpy as np
import json
import pickle
from flask import Flask,render_template,url_for,request

with open('columns.json','r') as f:
     __data_columns=json.load(f)['data_columns']
     __locations=__data_columns[3:]
   

def predict_price(location,sqft,bath,bhk):
    loc_index=__data_columns.index(location)
    x=np.zeros(244)
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    
    return model.predict([x])[0]

model=pickle.load(open('banglore_house_price_model.pickle','rb'))

app=Flask(__name__)

@app.route('/')

def main():
    return render_template('home.html',data=__locations)
@app.route('/predict',methods=['POST'])
def home():
    location=request.form['location']
    sqft=request.form['sqft']
    bhk=request.form['bhk']
    bath=request.form['bath']
    a=predict_price(location,sqft,bath,bhk)
    a=round(a,2)
    
    return render_template('after.html',data=a)





if __name__=='__main__':
    app.run(debug=True)