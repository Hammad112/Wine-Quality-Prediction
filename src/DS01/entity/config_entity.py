from dataclasses import dataclass
from pathlib import Path

## Data Ingestion
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir:Path

## Data Validation
@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict

## Data Transformation
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_file: Path  
