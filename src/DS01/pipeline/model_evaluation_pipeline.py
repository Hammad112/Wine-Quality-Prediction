from src.DS01.config.configuration import ConfigurationManager
from src.DS01.components.model_evaluation import ModelEvaluation
from src.DS01 import logger 
from pathlib import Path



STAGE_NAME='Model Evaluation Pipeline stage'

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
       
    def intiate_model_evaluation(self):
        try:
            config=ConfigurationManager()
            model_evaluation_config=config.get_model_evaluation_config()
            model_evaluation=ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise e

       



