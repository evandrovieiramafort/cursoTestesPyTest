import pytest
import requests
from unittest.mock import MagicMock


@pytest.fixture
def mock_response():
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value = {"mensagem": "Sucesso"}
    return mock

def test_chamada_api_com_mock_1(mock_response):
    response = mock_response
    assert response.status_code == 200
    assert response.status_code != 400
    assert response.json() == {"mensagem": "Sucesso"}
    assert response.json () != {"mensagem": "Erro"}

def test_chamada_api_com_mock_2(mock_response):
    response = mock_response
    assert response.status_code == 200
    assert response.status_code != 400
    assert response.json() == {"mensagem": "Sucesso"}
    assert response.json () != {"mensagem": "Erro"}