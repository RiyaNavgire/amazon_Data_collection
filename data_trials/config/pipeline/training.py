from time import strftime
from data_trials.entity.metadata_entity import DataIngestionMetadata
from data_trials.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from data_trials.constant.training_pipeline_config import *
from data_trials.constant import TIMESTAMP
from utils import create_directories
from data_trials.logger import logger
from data_trials.exception import DataTrialException
import os, sys
import requests
import json
from datetime import datetime
from data_trials.entity.metadata_entity import DataIngestionMetadata



class DataConfig:

    def __init__(self, pipeline_name=PIPELINE_NAME, timestamp=TIMESTAMP):
        self.timestamp = timestamp
        self.pipeline_name = pipeline_name
        self.pipeline_config = self.get_pipeline_config()

    def get_pipeline_config(self) -> TrainingPipelineConfig:
        """
        This function will provide pipeline config information


        returns > PipelineConfig = namedtuple("PipelineConfig", ["pipeline_name", "artifact_dir"])
        """
        try:
            artifact_dir = PIPELINE_ARTIFACT_DIR
            pipeline_config = TrainingPipelineConfig(pipeline_name=self.pipeline_name,
                                                     artifact_dir=artifact_dir)

            logger.info(f"Pipeline configuration: {pipeline_config}")

            return pipeline_config
        except Exception as e:
            raise DataTrialException(e, sys)

    def get_data_ingestion_config(self)-> DataIngestionConfig:

        
        """
        master directory for data ingestion
        we will store metadata information and ingested file to avoid redundant download
        """
        data_ingestion_master_dir = os.path.join(self.pipeline_config.artifact_dir,
                                                 DATA_INGESTION_DIR)

        # time based directory for each run
        data_ingestion_dir = os.path.join(data_ingestion_master_dir,
                                          self.timestamp)

        metadata_file_path = os.path.join(data_ingestion_master_dir, DATA_INGESTION_METADATA_FILE_NAME)

        data_ingestion_metadata = DataIngestionMetadata(metadata_file_path=metadata_file_path)

        if data_ingestion_metadata.is_metadata_file_present:
            metadata_info = data_ingestion_metadata.get_metadata_info()
            

        data_ingestion_config = DataIngestionConfig(
            data_ingestion_dir=data_ingestion_dir,
            download_dir=os.path.join(data_ingestion_dir, DATA_INGESTION_DOWNLOADED_DATA_DIR),
            file_name=DATA_INGESTION_FILE_NAME,
            feature_store_dir=os.path.join(data_ingestion_master_dir, DATA_INGESTION_FEATURE_STORE_DIR),
            failed_dir=os.path.join(data_ingestion_dir, DATA_INGESTION_FAILED_DIR),
            metadata_file_path=metadata_file_path,
            datasource_url=DATA_INGESTION_DATA_SOURCE_URL
            
        )
    
        logger.info(f"Data ingestion config: {data_ingestion_config}")
        return data_ingestion_config

    

    
    

