from src.DS01.config.configuration import ConfigurationManager
from src.DS01.components.model_trainer import ModelTrainer
from src.DS01 import logger
from pathlib import Path


STAGE_NAME='Model Training stage'

class ModelTrainingPipeline:
    def __init__(self):
        pass
       
    def intiate_model_training(self):
        try:
            config=ConfigurationManager()
            model_trainer_config=config.get_model_trainer_config()
            model_trainer=ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e
       
