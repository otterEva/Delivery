import pytest
import pytest_asyncio
from unittest.mock import patch, AsyncMock, MagicMock

from app.services.gis_responce import GetGisResponce


@pytest_asyncio.fixture
async def request_list():
    return [
        {
            "points": [{"lat": 55.75, "lon": 37.62}, {"lat": 55.76, "lon": 37.64}],
            "sources": [0],
            "targets": [1],
            "real_sources": 0,
            "real_targets": [1]
        }
    ]


@pytest.mark.asyncio
async def test_gather_2gis_list_responce(request_list):
    gis_service = GetGisResponce()
    mock_post_response = AsyncMock()
    mock_post_response.json = MagicMock(return_value={"task_id": "12345"})
    mock_get_status = AsyncMock()
    mock_get_status.json = MagicMock(return_value={
        "status": "TASK_DONE",
        "result_link": "https://fake-link.com"
    })
    mock_get_result = AsyncMock()
    mock_get_result.content = b'{"routes": [{"distance": 999, "duration": 88}]}'
    with patch("httpx.AsyncClient.post", return_value=mock_post_response), \
            patch("httpx.AsyncClient.get", side_effect=[mock_get_status, mock_get_result]):
        response = await gis_service.gather_2gis_list_responce(request_list)

        assert "routes" in response
        assert len(response["routes"]) == 1

        json_part, indexes_data = response["routes"][0]

        assert json_part["routes"][0]["distance"] == 999
        assert json_part["routes"][0]["duration"] == 88

        assert indexes_data["real_sources"] == 0
        assert indexes_data["real_targets"] == [1]


@pytest.mark.asyncio
async def test_gather_2gis_list_responce_no_task_id(request_list):
    gis_service = GetGisResponce()
    mock_post_response = AsyncMock()
    mock_post_response.json = MagicMock(return_value={"error": "some error"})
    with patch("httpx.AsyncClient.post", return_value=mock_post_response):
        with pytest.raises(Exception) as exc_info:
            await gis_service.gather_2gis_list_responce(request_list)

        assert "2gis says" in str(exc_info.value)
