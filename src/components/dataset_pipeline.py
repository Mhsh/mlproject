import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import ApplicationException
from src.logger import logging
from src.utils import save_object
import os

@dataclass
class DatasetPipelineConfig:
    pre_processor_path=os.path.join("model_artifacts","pre_processor.pkl")

class DatasetPipeline:
    def __init__(self,numerical_columns,categorical_columns) -> None:
        self.numerical_columns = numerical_columns
        self.categorical_columns = categorical_columns
        self.data_set_pipeline_config=DatasetPipelineConfig()

    def create_pipeline(self):
        try:
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {self.categorical_columns}")
            logging.info(f"Numerical columns: {self.numerical_columns}")
            logging.info(f"Created pipeline-----")
            logging.info(f"{num_pipeline} - {cat_pipeline}")
            logging.info(f"---------------------")
            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,self.numerical_columns),
                ("cat_pipelines",cat_pipeline,self.categorical_columns)

                ]
            )
            return preprocessor
        except Exception as e:
               raise ApplicationException(e,sys)
        