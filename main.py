from src.DS01 import logger
from src.DS01.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DS01.pipeline.data_validation_pipeline import DataValidationTrainingPipeline


STAGE_NAME='Data Ingestion stage'

try:
    logger.info(f"Initiating {STAGE_NAME} Started")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.intiate_data_ingestion()
    logger.info(f"Completed {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Data Validation stage'

try:
    logger.info(f"Initiating {STAGE_NAME} Started")
    data_validation=DataValidationTrainingPipeline()
    data_validation.intiate_data_validation()
    logger.info(f"Completed {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

