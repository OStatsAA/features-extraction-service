import pytest
import unittest.mock as mocker
import pandas as pd
import os
from src.extractor.features_extractor import FeaturesExtractor, DataFeaturesSet
from src.service import Service
import src.service.features_extractor_service_pb2 as pb2

@pytest.fixture
def testing_dataframe() -> pd.DataFrame:
    return pd.DataFrame({
        'V1': ['Row1', 'Row2', 'Row3'],
        'V2': [1, 1, 1],
        'V3': [True, False, True],
        'V4': [123, 123, 123]})


@pytest.fixture
def testing_dataframe_features(testing_dataframe) -> DataFeaturesSet:
    return FeaturesExtractor().run(testing_dataframe, 'V4')


@pytest.fixture
def db_mock(testing_dataframe_features: DataFeaturesSet) -> mocker.Mock:
    mock = mocker.Mock()
    attrs = {
        'get_features.return_value': testing_dataframe_features,
        'save_features.return_value': None
    }
    mock.configure_mock(**attrs)
    return mock


def test_get_features_should_return_a_protobuf_instance(db_mock: mocker.Mock) -> None:
    service = Service(db_mock)
    request = pb2.GetFeaturesRequest(dataset_id= 'test')
    pb2_features = service.GetFeatures(request, None)
    assert isinstance(pb2_features, pb2.DataFeaturesSet)


def test_extract_features_should_return_protobuf_instance(db_mock: mocker.Mock, testing_dataframe: pd.DataFrame) -> None:
    service = Service(db_mock)
    testing_dataframe.to_hdf('test.h5', 'dataset')
    request = pb2.ExtractFeaturesRequest(dataset_id= 'test', response_name= 'V4')
    pb2_features = service.ExtractFeatures(request, None)
    os.remove('test.h5')
    assert isinstance(pb2_features, pb2.DataFeaturesSet)