import pytest
import requests
from main import get_temperature


class Mock():

    @staticmethod
    def json():
        return {'currently': {'temperature': 62}}


@pytest.fixture
def mock_response(monkeypatch):
    def mock(*args, **kwargs):
        return Mock()

    monkeypatch.setattr(requests, 'get',  mock)


def test_get_temperature_by_lat_lng(mock_response):
    result = get_temperature(-14.235004, -51.92528)

    assert result == 16
