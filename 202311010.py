from flask import Flask, render_template, request
import pandas as pd
import joblib
from keras.models import load_model

app = Flask(__name__)

# Load models and data
model4s = load_model("model_4s.h5")
model6s = load_model("model_6s.h5")
modelwkt = load_model("modelwkt.h5")
# model4s = joblib.load('model_4.pkl')
# model6s = joblib.load('model_6.pkl')
# modelwkt = joblib.load('modelwkt.pkl')

name_data = pd.read_csv('name.csv')
country_data = pd.read_csv('countries.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_id = request.form['id']
    user_opposite = request.form['opposite']
    user_R = float(request.form['R'])
    user_B = float(request.form['B'])
    user_M = float(request.form['M'])
    user_o = float(request.form['o'])

    user_number = name_data[name_data['BATTING'] == user_id]['ID'].values[0]
    user_team = name_data[name_data['BATTING'] == user_id]['Team'].values[0]
    user_opp = country_data[country_data['Team'] == user_opposite]['ID'].values[0]

    input_46s = [[user_R, user_B, user_M, user_number, user_opp]]
    predicted_4s = model4s.predict(input_46s)[0]
    predicted_6s = model6s.predict(input_46s)[0]

    input_wkts = [[int(user_number),int(user_opp) , user_o]]

    predicted_wickets =  modelwkt.predict(input_wkts)[0] 

    return render_template('result.html', predicted_4s=int(abs(predicted_4s%50)),
                           predicted_6s=int(abs(predicted_6s%40)), predicted_wickets=int(predicted_wickets%10))

if __name__ == '__main__':
    app.run(debug=True)
