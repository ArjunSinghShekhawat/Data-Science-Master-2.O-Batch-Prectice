from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

ridge_model = pickle.load(open('E:\Pandas\Algerian Forest Fires Project\Models\\ridge.pkl','rb'))
standard_scaler = pickle.load(open('E:\Pandas\Algerian Forest Fires Project\Models\scaler.pkl','rb'))

#route for home page
app.route('/')
def index():
    return render_template('Algerian Forest Fires Project//templates//index.html')




if __name__=='__main__':
    app.run(host='0.0.0.0')