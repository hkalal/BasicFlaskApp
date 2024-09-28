import sys
import pandas as pd
import os
import pickle

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path= os.path.join("artifacts","model.pkl")
            preprocessor_path= os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")
            model=self.load_objectload_object(file_path=model_path)
            preprocessor=self.load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            pass


    def load_object(self,file_path):
        try:
            with open(file_path, "rb") as file_obj:
                return pickle.load(file_obj)

        except Exception as e:
            pass