from components.dataset_split import DataSetSplitter
from components.dataset_pipeline import DatasetPipeline
from components.dataset_transformation import DataSetTransformation
from components.model_trainer import ModelTrainer
from src.logger import logging
from src.yaml_reader import YamlReader


if __name__=="__main__":
    model_struct = YamlReader()
    dataset_path = model_struct.get_dataset()
    target_feature_name = model_struct.get_target_feature()

    # create column transformer pipeline for data.
    pipeline_obj=DatasetPipeline(model_struct.get_numerical_column(), 
                                model_struct.get_categorical_columns()).create_pipeline()

    # split the data.
    dataset_splitter = DataSetSplitter(dataset_path)
    train_data_path, test_data_path = dataset_splitter.split_dataset()

    # transform the data for model training after applying pipeline.
    data_transformation=DataSetTransformation(train_data_path,
                                            test_data_path,target_feature_name)
    train_arr,test_arr=data_transformation.transform_data(pipeline_obj)

    # start model training.
    modeltrainer = ModelTrainer()
    modeltrainer.create_model(train_arr,test_arr)

