import pytest
from unittest.mock import MagicMock
from jev_ultrafast.browser import StalePageException
# Adjust the import match according to how your guard logic is exposed
from scripts.check_guards import check_page_freshness  

@pytest.fixture
def offline_data_url_fixture():
    """Provides a safe, static offline data URL context simulating a page structure."""
    mock_browser = MagicMock()
    mock_browser.current_url = "data:text/html,<html><body><div id='test'></div></body></html>"
    return mock_browser

def test_guard_page_freshness_success(offline_data_url_fixture):
    """Asserts that guard validation passes on a completely fresh, matching page context."""
    # Should run and exit cleanly without raising errors
    check_page_freshness(offline_data_url_fixture, expected_element="test")

def test_guard_page_freshness_stale_raises_exception(offline_data_url_fixture):
    """Asserts that guard validation raises a StalePageException if the signature mismatches."""
    # Modify mock state to simulate a stale reference error
    offline_data_url_fixture.current_url = "data:text/html,<html><body></body></html>"
    
    with pytest.raises(StalePageException):
        check_page_freshness(offline_data_url_fixture, expected_element="test")
