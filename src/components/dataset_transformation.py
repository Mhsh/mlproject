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
from src.components.dataset_split import DataSetSplitter
import os
from src.utils import save_object

class DataSetTransformation:
    def __init__(self,train_path,test_path,target_column_name) -> None:
        self.train_path = train_path
        self.test_path = test_path
        self.target_column_name = target_column_name
        self.pre_processor_path=os.path.join("model_artifacts","pre_processor.pkl")
        
    def transform_data(self, preprocessing_obj: ColumnTransformer):

        try:
            train_df=pd.read_csv(self.train_path)
            test_df=pd.read_csv(self.test_path)

            logging.info("Reading train and test dataset for applying the transformation pipeline")

            input_feature_train_df=train_df.drop(columns=[self.target_column_name],axis=1)
            target_feature_train_df=train_df[self.target_column_name]

            input_feature_test_df=test_df.drop(columns=[self.target_column_name],axis=1)
            target_feature_test_df=test_df[self.target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info("Successfully applied the pipeline.")
            save_object(
                file_path=self.pre_processor_path,
                obj=preprocessing_obj
            )
            return (
                train_arr,
                test_arr
            )
        except Exception as e:
            raise ApplicationException(e,sys)
