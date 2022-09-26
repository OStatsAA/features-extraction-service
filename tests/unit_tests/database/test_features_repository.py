import pytest
import unittest.mock as mocker

from src.database.features_repository import FeaturesRepository
from src.extractor.features_set import DataFeaturesSet


@pytest.fixture
def db_mock() -> mocker.Mock:
    mock = mocker.Mock()
    attrs = {
        'get.return_value': DataFeaturesSet(),
        'set.return_value': None
    }
    mock.configure_mock(**attrs)
    return mock


def test_should_call_get_method_once(db_mock: mocker.Mock) -> None:
    repository = FeaturesRepository(db_mock)
    dataset_id = 'test'
    features = repository.get_features(dataset_id)
    db_mock.get.assert_called_once_with(dataset_id)
    assert isinstance(features, DataFeaturesSet)


def test_should_call_set_method_once(db_mock: mocker.Mock) -> None:
    repository = FeaturesRepository(db_mock)
    dataset_id = 'test'
    features = DataFeaturesSet()
    repository.save_features(dataset_id, features)
    db_mock.set.assert_called_once_with(dataset_id, features)
