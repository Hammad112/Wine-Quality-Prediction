import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.DS01 import logger
from src.DS01.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config=config
    
    ## We Can add different data transformation techniques such as scalar,
    ## PCA and ALL

    ## We can perform EDA here before passing the data to model
    ## For this project I'm just splitting data into train and test set
    
    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_file)
        train,test=train_test_split(data,test_size=0.2,random_state=42)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splitted data into test and train set")
        logger.info(train.shape)
        logger.info(test.shape)

        print(test.shape)
        print(train.shape)