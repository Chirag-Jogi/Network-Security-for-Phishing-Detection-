from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_tranformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
import sys
if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestioncofig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestioncofig)
        logging.info('Initiate the data ingestion')
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate Data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("Initiate Data tranformation")
        data_tranformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_tranformation_artifact=data_tranformation.initiate_data_transformation()
        print(data_tranformation_artifact)
        logging.info("data tranformation completed")

        logging.info("Model training started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_tranformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model training artifact created")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)