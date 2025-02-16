import os
import yaml
from src.DS01 import logger
import json
import joblib
## it make sure what type is expected will be returned 
## like ConfigBox is required it will check for 
## if it return in ConfigBox format then right else
## it would give an error other then displaying anything undesired 
from ensure import ensure_annotations
## yamls file in key value pairs
## Cogig box is used so that we can call directly by key
## else it's not allowed in python
from box import ConfigBox
from pathlib import Path 
from typing import Any
## Exception Handling
from box.exceptions import BoxValueError


## Reading Yaml File Saving in Config File 
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reading Yamls file and Returns ConfigBox type    
    
    Args :
        path_to_yaml : Path to yaml file
    
    Raises:
            ValueError: Yaml is empty
            e : empty file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            ## Reading Yaml File 
            content=yaml.safe_load(yaml_file)
            ## Logs
            logger.info(f"yaml file :{path_to_yaml} loaded sucessfully")
       
        return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e


## Create Directories
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
    Create list of Directories     
    Args:
        path_to_dirs (list) : list of Path of directories
        ignore_log (bool,optional): ignore if multiple dirs is to created .Defaults to
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")

## Save Json Format
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save data in json format
    
    Args:
        path: Path to json file
        data (dict) : data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data,f, indent=4)
        logger.info(f"Data saved in json format at {path}")


## Load Json Format
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load data in json format
    
    Args:
    path: Path to json file

    Returns:
        ConfigBox: Data in ConfigBox format
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"Data loaded from json file {path}")
    return ConfigBox(content)

## Save Model
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file
        
    Args:
        data (Any): data to be saved as binary
        Path (Path): Path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Model saved at {path}")

## Loading Saved Model
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file
    
    Args:
        path (Path): Path to binary file
    
    Returns:
        Any: Data loaded from binary file
    """
    data = joblib.load(path)
    logger.info(f"Model loaded from {path}")
    return data