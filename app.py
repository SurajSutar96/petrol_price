from flask import Flask,render_template,request,jsonify
import pickle
with open('Petrol_model.pkl','rb')as f:
    model=pickle.load(f)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    array=[float(x) for x in request.form.values()]
    pred=model.predict([array])[0]
    return render_template('home.html',prediction_text=f"Predicted price of petrol is :- {pred} $")

if __name__=="__main__":
    app.run(port='4444',debug=True)