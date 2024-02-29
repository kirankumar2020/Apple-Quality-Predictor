from flask import Flask,request,render_template,url_for,jsonify
import json
import pickle
from utils import get_apple_quality
from config import PORT_NUMBER



app = Flask(__name__)


@app.route('/home',methods = ["GET","POST"])
def home():

    return render_template("index.html")

@app.route("/apple_quality",methods=["GET", "POST"])
def apple_quality():
    # result  = None
    if request.method == "POST":
       data = request.form
       Size = eval(data["Size"])
       Weight = eval(data["Weight"])
       Sweetness = eval(data["Sweetness"])
       Crunchiness = eval(data["Crunchiness"])
       Juiciness = eval(data["Juiciness"])
       Ripeness = eval(data["Ripeness"])
       Acidity = eval(data["Acidity"])

       result = get_apple_quality(Size,Weight,Sweetness,Crunchiness,Juiciness,Ripeness,Acidity)

       return render_template("index.html",prediction = result)

    # return jsonify({"response":"successful",
    #                 "result":f"Predicted price of mobile is : {result}"})
    # return jsonify({"prediction": result})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",PORT_NUMBER = 8080,debug = False)



#     @app.route("/apple_quality", methods=["GET", "POST"])
# def apple_quality():
#     print(request.method)  # Print the request method to console
#     ...
