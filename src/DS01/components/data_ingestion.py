import urllib.request as request
import os
from src.DS01 import logger
import zipfile
from src.DS01.entity.config_entity import (DataIngestionConfig)

## Data Ingestion Component

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    ## Downloading gthe Zip File
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info : \n {headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists ")


   ## Extracting Zip file
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
            
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
           