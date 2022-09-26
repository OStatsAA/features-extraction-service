"""Features Extractor Service running on GRPC"""

from typing import Any
from src.database import FeaturesRepository
from src.extractor import FeaturesExtractor, DataFeaturesSet
from src.storage import get_data_from_storage

import src.service.features_extractor_service_pb2_grpc as pb2_grpc
import src.service.features_extractor_service_pb2 as pb2


class Service(pb2_grpc.FeaturesExtractorServiceServicer):
    """Service implementation extending protobuf servicer

    Args:
        pb2_grpc (FeaturesExtractorServiceServicer): GRPC Server
    """

    def __init__(self, db: FeaturesRepository) -> None:
        self.__db = db

    def GetFeatures(self, request: pb2.GetFeaturesRequest, context: Any) -> pb2.DataFeaturesSet:
        """Get dataset features stored in database

        Args:
            request (GetFeaturesRequest): GetFeaturesRequest protobuf
            context (_type_): _description_

        Returns:
            DataFeaturesSet: Data FeaturesSet protobuf
        """
        features = self.__db.get_features(request.dataset_id)
        protobuf_response = self.__map_features_to_protobuf_response(features)
        return protobuf_response

    def ExtractFeatures(self, request: pb2.ExtractFeaturesRequest, context: Any) -> pb2.DataFeaturesSet:
        """Extracts features from dataset, saves in database and return extracted features

        Args:
            request (ExtractFeaturesRequest): Extract Features Request protobuf
            context (_type_): _description_

        Returns:
            DataFeaturesSet: Data FeaturesSet protobuf
        """
        dataframe = get_data_from_storage(request.dataset_id)
        features = FeaturesExtractor().run(dataframe, request.response_name)
        protobuf_response = self.__map_features_to_protobuf_response(features)
        self.__db.save_features(request.dataset_id, features)
        return protobuf_response

    def __map_features_to_protobuf_response(self, features: DataFeaturesSet) -> pb2.DataFeaturesSet:

        pb2_msg = pb2.DataFeaturesSet()
        pb2_msg.rows_count = features.rows_count
        pb2_msg.variables_count = features.variables_count
        pb2_msg.ratio_of_continous_variables = features.ratio_of_continous_variables
        pb2_msg.is_response_quantitative = features.is_response_quantitative
        pb2_msg.is_response_dichotomous = features.is_response_dichotomous

        for (var_name, var_features) in features.variables_features_set.items():
            pb2_var_features = pb2_msg.variables_features_set.get_or_create(
                var_name)
            pb2_var_features.is_quantitative = var_features.is_quantitative
            pb2_var_features.missing_entries_ratio = var_features.missing_entries_ratio

        return pb2_msg
