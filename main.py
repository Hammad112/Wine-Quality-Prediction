from src.DS01 import logger
from src.DS01.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DS01.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.DS01.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DS01.pipeline.model_trainer_pipeline import ModelTrainingPipeline



## data Ingestion 

STAGE_NAME='Data Ingestion stage'

try:
    logger.info(f"Initiating {STAGE_NAME} Started")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.intiate_data_ingestion()
    logger.info(f"Completed {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e


## Data Validation

STAGE_NAME='Data Validation stage'

try:
    logger.info(f"Initiating {STAGE_NAME} Started")
    data_validation=DataValidationTrainingPipeline()
    data_validation.intiate_data_validation()
    logger.info(f"Completed {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e


## Data Transformation

STAGE_NAME='Data Transformation stage'

try:
    logger.info(f"Initiating {STAGE_NAME} Started")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.intiate_data_transformation()
    logger.info(f"Completed {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

## Model Training
STAGE_NAME='Data Transformation stage'

try:
    logger.info(f"Initiating {STAGE_NAME} Started")
    data_transformation=ModelTrainingPipeline()
    data_transformation.intiate_model_training()
    logger.info(f"Completed {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e


