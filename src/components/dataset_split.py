import os
import sys
from src.exception import ApplicationException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataSetSplitterConfig:
    train_data_path: str=os.path.join('model_artifacts',"train.csv")
    test_data_path: str=os.path.join('model_artifacts',"test.csv")
    raw_data_path: str=os.path.join('model_artifacts',"raw_data.csv")

class DataSetSplitter:
    def __init__(self, data_set_path):
        self.data_set_prepare_config=DataSetSplitterConfig()
        self.data_path = data_set_path

    def split_dataset(self):
        logging.info("Starting to split dataset in test and train dataset")
        try:
            df=pd.read_csv(self.data_path)
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.data_set_prepare_config.train_data_path),exist_ok=True)

            df.to_csv(self.data_set_prepare_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=47)

            train_set.to_csv(self.data_set_prepare_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.data_set_prepare_config.test_data_path,index=False,header=True)

            logging.info(f'''Split is completed with train at {self.data_set_prepare_config.train_data_path} 
                                 and test data at {self.data_set_prepare_config.train_data_path}  location''')
            return(
                self.data_set_prepare_config.train_data_path,
                self.data_set_prepare_config.test_data_path

            )
        except Exception as e:
            raise ApplicationException(e,sys)
        


