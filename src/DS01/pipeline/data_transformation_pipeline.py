from src.DS01.config.configuration import ConfigurationManager
from src.DS01.components.data_transformation import DataTransformation
from src.DS01 import logger
from pathlib import Path



STAGE_NAME='Data Transformation stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
       
    def intiate_data_transformation(self):
        # Read and check both validation statuses
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                statuses = f.readlines()
                column_status = statuses[0].strip().split(" ")[-1]
                data_type_status = statuses[1].strip().split(" ")[-1]
            
            if column_status == "True" and data_type_status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data schema or data types are not valid")

        except Exception as e:
            print(e)
       



