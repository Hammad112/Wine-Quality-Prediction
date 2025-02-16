from src.DS01.config.configuration import ConfigurationManager
from src.DS01.components.data_ingestion import DataIngestion
from src.DS01 import logger



STAGE_NAME='Data Ingestion stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
       
    def intiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
       
if __name__=='__main__':
    try:
        logger.info(f"Initiating {STAGE_NAME} Started")
        obj=DataIngestionTrainingPipeline()
        obj.intiate_data_ingestion()
        logger.info(f"Completed {STAGE_NAME} Completed")
    except Exception as e:
        loggerexception(e)
        raise e