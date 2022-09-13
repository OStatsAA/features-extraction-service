"""
Feature Extractor Class
"""
from numpy.typing import NDArray

from .features_set import FeaturesSet

class FeatureExtractor:
    """
    Feature Extractor class
    """
    features_set: FeaturesSet

    def __init__(self, features_set: FeaturesSet = FeaturesSet):
        self.features_set = features_set

    def run(self, data: NDArray):
        """Extracts features from providaded data

        Args:
            data (NDArray): dataset

        Returns:
            Dataset: _description_
        """
        self.features_set.rows_count = len(data)
