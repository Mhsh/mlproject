
from src.logger import logging
import sys
import yaml
from yaml.loader import SafeLoader
from src.exception import ApplicationException

class YamlReader:
    def __init__(self):
        if(sys.argv.__len__()==1):
            raise ApplicationException("Please pass settings.yml path.",sys)
        logging.info(f'Arguments passed {sys.argv}')
        logging.info(f'Trying to read configuration file (settings.yml) from location {sys.argv[1]}')
        with open(sys.argv[1]) as f:
            self.yml = yaml.load(f, Loader=SafeLoader)
        logging.info(f'settings.yml read succesfully and contains property as {self.yml}')

    def get_dataset(self):
        return self.yml.get('dataset')

    def get_target_feature(self):
        return self.yml.get('target_feature')
    
    def get_numerical_column(self):
        return self.yml.get('numerical_columns')

    def get_categorical_columns(self):
        return self.yml.get('categorical_columns')