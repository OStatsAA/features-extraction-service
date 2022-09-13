"""
Feature Extractor Testing
"""

import numpy as np

from feature_extractor.extractor import FeatureExtractor

def test_should_set_total_rows_count():
    """Testing total rows count"""
    data = np.array([
        ('Row1', 1, 123),
        ('Row1', 1, 123),
        ('Row1', 1, 123),
    ], dtype=[('V1', str), ('V2', int), ('V3', int)])

    feature_extractor = FeatureExtractor()
    feature_extractor.run(data)

    assert feature_extractor.features_set.rows_count == 3
    