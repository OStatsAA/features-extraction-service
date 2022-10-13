from redis import Redis

from ostatslib.features_extractor import DataFeaturesSet


class FeaturesRepository:
    """Repository for get and set features to database
    """

    def __init__(self, db: Redis) -> None:
        self.__db = db

    def get_features(self, dataset_id: str) -> DataFeaturesSet:
        """Get dataset features

        Args:
            dataset_id (str): Dataset ID

        Returns:
            DataFeaturesSet: features for the requested dataset
        """
        return self.__db.get(dataset_id)

    def save_features(self, dataset_id: str, features: DataFeaturesSet) -> None:
        self.__db.set(dataset_id, features)
