from flask import Flask,request, render_template
from flask_restful import Resource, Api
import pickle
import pandas as pd
from flask_cors import CORS

model = pickle.load(open("model - Copy.pkl", "rb"))


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("checkbox_form.html")



@app.route("/predict", methods=["POST"])
def predict():
    data = ["0"]*14
    columns = ['Car_Owner', 'CHILDREN', 'Annual_income', 'EDUCATION', 'Employed_days', 'Family_Members','F', 'M', 'Property_Owner', 'Civil marriage', 'Married', 'Separated', 'Single / not married','Widow']
    if request.method == "POST":
        for i in range(len(columns)):
            if(request.form.get(columns[i]) == None):
                data[i] = 0
            elif(request.form.get(columns[i]) == "on"):
                data[i] = 1
            else:
                data[i] = int(request.form.get(columns[i]))
    
    df = pd.DataFrame([data], columns=columns)
    predictions = model.predict(df)
    print(predictions[0])

    return render_template('checkbox_form.html', predictions = predictions)


if __name__ == '__main__':

    app.run(debug=True)