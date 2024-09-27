import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_internet_value, mock_valid_url_value, expected_result, url",
    [
        (True, True, "Accessible", "https://www.google.com"),
        (False, True, "Not accessible", "https://www.google.com"),
        (True, False, "Not accessible", "https://invalid-url.com"),
        (False, False, "Not accessible", "https://invalid-url.com"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet: callable, mock_valid_url: callable,
                                mock_internet_value: callable, mock_valid_url_value: callable,
                                expected_result: callable, url: callable) -> None:
    mock_internet.return_value = mock_internet_value
    mock_valid_url.return_value = mock_valid_url_value

    result = can_access_google_page(url)
    assert result == expected_result
