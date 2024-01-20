from flask import Flask,jsonify,render_template,request,url_for,redirect
import config
from project_app.utils import MedicalInsurance

app=Flask(__name__)
@app.route("/")
def my_fun():
    print("Hello Flask!")
    return render_template("home.html")
def get_insurance_charges():
    data=request.form
    print("Data is:",data)

    age=eval(data["age"])
    sex=data["sex"]
    bmi=eval(data["bmi"])
    children=eval(data["children"])
    smoker=data["smoker"]
    region=data["region"]

    print("age,sex,bmi,children,smoker,region >>",age,sex,bmi,children,smoker,region)

    meds_ins=MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges=meds_ins.get_predict_charges()

    return jsonify({"Result":f"Predicted Medical Insurance charges are {charges}"})

app.run(port=config.PORT_NUMBER,debug=True)
