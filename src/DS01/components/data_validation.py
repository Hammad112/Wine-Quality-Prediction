import os
from src.DS01 import logger
import pandas as pd
from src.DS01.entity.config_entity import (DataValidationConfig)


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validates if all columns in the dataset match the expected schema.
        Updates the status file accordingly.
        """
        try:
            validation_status = True  # Assume valid initially

            # Read dataset
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            # Check if any column is missing or extra
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    f.write(f"Column validation status: {validation_status}\n")

            # Append column validation status to the status file
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Column validation status: {validation_status}\n")

            return validation_status

        except Exception as e:
            raise e

    def validate_data_types(self) -> bool:
        """
        Validates if the data types of the dataset match the expected schema.
        Updates the status file accordingly.
        """
        try:
            validation_status = True  # Assume valid initially

            # Read dataset
            data = pd.read_csv(self.config.unzip_data_dir)
            all_schema = self.config.all_schema

            # Check data types
            for col_name, col_type in all_schema.items():
                if col_name in data.columns and data[col_name].dtype != col_type:
                    validation_status = False
                    f.write(f"Data type validation status: {validation_status}\n")

            # Append data type validation status to the status file
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Data type validation status: {validation_status}\n")

            return validation_status

        except Exception as e:
            raise e
