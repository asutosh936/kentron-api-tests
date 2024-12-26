import os
import pytest
import logging
from auth_helpers import get_auth_token


# Configure logging
def setup_logging():
    """
    Configures logging for the test suite.
    Logs will be stored in a file and printed on the console.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("test_logs.log"),  # Log to file
            logging.StreamHandler()  # Log to console
        ],
    )
    logging.info("Logging setup complete.")


# Set up global fixtures
@pytest.fixture(scope="session", autouse=True)
def global_setup_and_teardown():
    """
    Fixture to run global setup and teardown for the test suite.
    This will execute once per test session.
    """
    setup_logging()
    logging.info("Starting Test Suite Execution")
    yield
    logging.info("Test Suite Execution Completed")


@pytest.fixture(scope="session")
def auth_token():
    """
    Fixture to provide an authentication token for API requests.
    This fixture is scoped to the session level,
    meaning it runs only once per session.
    """
    try:
        token = get_auth_token()
        logging.info("Authentication token generated successfully.")
        return token
    except Exception as e:
        logging.error(f"Failed to generate authentication token: {e}")
        pytest.fail("Authentication token generation failed.", pytrace=False)


@pytest.fixture
def base_url():
    """
    Fixture to provide the base URL for API endpoints.
    This ensures that the base URL is consistent across all tests.
    """
    print("Setting base URL %s", os.getenv("API_BASE_URL"))
    url = os.getenv("API_BASE_URL")
    # url = "https://backend-dev.kentron.ai/api/v1"
    logging.info(f"Base URL set to: {url}")
    return url


# Log test start and end
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Log the start of each test."""
    logging.info(f"Starting test: {item.name}")


@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    """Log the completion of each test."""
    logging.info(f"Completed test: {item.name}")
