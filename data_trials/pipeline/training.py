from data_trials.exception import DataTrialException
from data_trials.logger import logger
from data_trials.config.pipeline.training import DataConfig
from data_trials.component import DataIngestion
from data_trials.entity.artifact_entity import DataIngestionArtifact
import sys


class TrainingPipeline:

    def __init__(self, data_config: DataConfig):
        self.finance_config: DataConfig = data_config

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = self.finance_config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            return data_ingestion_artifact

        except Exception as e:
            raise DataTrialException(e, sys)

    

    def start(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
           # data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
           # data_transformation_artifact = self.start_data_transformation(
            #    data_validation_artifact=data_validation_artifact)
            #model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            #model_eval_artifact = self.start_model_evaluation(data_validation_artifact=data_validation_artifact,
             #                                                 model_trainer_artifact=model_trainer_artifact )
            #if model_eval_artifact.model_accepted:
             #   self.start_model_pusher(model_trainer_artifact=model_trainer_artifact)
        except Exception as e:
            raise DataTrialException(e, sys)
