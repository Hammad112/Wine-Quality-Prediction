from src.DS01.components.data_validation import DataValidation
from src.DS01 import logger
from src.DS01.config.configuration import ConfigurationManager

STAGE_NAME='Data Validation stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
       
    def intiate_data_validation(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_data_types()
       
if __name__=='__main__':
    try:
        logger.info(f"Initiating {STAGE_NAME} Started")
        obj=DataValidationTrainingPipeline()
        obj.intiate_data_validation()
        logger.info(f"Completed {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e