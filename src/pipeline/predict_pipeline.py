import sys
import pandas as pd
from src.exception import ApplicationException
from src.utils import load_object
from pydantic import BaseModel
import os

class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("model_artifacts","model.pkl")
            preprocessor_path = os.path.join("model_artifacts","pre_processor.pkl")
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)
            print(features)
            data_scaled = preprocessor.transform(features)
            prediction = model.predict(data_scaled)
            return prediction
        except Exception as e:
            raise ApplicationException(e,sys)

class CustomData(BaseModel):
    gender:str
    race_ethnicity:str
    parental_level_of_education:str     
    lunch:str
    test_preparation_course:str
    writing_score:int
    reading_score:int
    class Config:
        schema_extra = {
            "example": {
                'gender':'male',
                'race_ethnicity': 'group B',
                'parental_level_of_education':'bachelor\'s degree',
                'lunch':'standard',
                'test_preparation_course':'none',
                'writing_score':72,
                'reading_score':72
            }
        }

    def get_dataframe(self,data):
        try:
            received = data.dict()
            self.gender = received['gender'], 
            self.race_ethnicity =received['race_ethnicity'],
            self.parental_level_of_education = received['parental_level_of_education'],
            self.lunch = received['lunch'],
            self.test_preparation_course = received['test_preparation_course'],
            self.writing_score = received[ 'writing_score'],
            self.reading_score = received['reading_score']
            data_frame = {
                'gender':self.gender,
                'race_ethnicity': self.race_ethnicity,
                'parental_level_of_education':self.parental_level_of_education,
                'lunch':self.lunch,
                'test_preparation_course':self.test_preparation_course,
                'writing_score':self.writing_score,
                'reading_score':self.reading_score
            }
            return pd.DataFrame(data_frame)
        except Exception as e:
            raise ApplicationException(e,sys)