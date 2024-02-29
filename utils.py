import pickle
import numpy as np
import pandas as pd
import json


def get_apple_quality(Size,Weight,Sweetness,Crunchiness,Juiciness,Ripeness,Acidity):
    mobile_path = r"Apple...KNN_clf_model.pkl"
    # mobile_path_json = r"Apple_Data\colum_data.json"

    with open(mobile_path, 'rb') as f:
        model=pickle.load(f)

        with open('colum_data.json', "r") as f:
           data = json.load(f)
       
    
        test_array = np.array([Size,Weight,Sweetness,Crunchiness,Juiciness,Ripeness,Acidity],ndmin=2)
    
        # test_array

        predicted_class = model.predict(test_array)[0]
        print("predicted_class :",predicted_class)
        Apple_quality = "Good" if predicted_class == 1 else "Bad"
        print("Quality of Apple is :", Apple_quality)

        return Apple_quality




# Size = 0.05
    # Weight = 1.68
    # Sweetness = 1.71
    # Crunchiness = 0.5
    # Juiciness = 2.1
    # Ripeness = 3.5
    # Acidity = 1.4