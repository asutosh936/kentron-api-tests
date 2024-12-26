import requests
import os


def get_auth_token():
    """Generates an authentication token."""
    url = os.getenv("API_BASE_URL") + "/auth/login/"
    # url = "https://backend-dev.kentron.ai/api/v1/auth/login/"
    credentials = {"email": os.getenv("USER_EMAIL"),
                   "password": os.getenv("USER_PASSWORD"),
                   "tenant_name": os.getenv("USER_TENANT")}
    response = requests.post(url, json=credentials)
    if response.status_code == 200:
        return response.json().get('data').get('access')
    raise Exception(f"Authentication failed! Status code: {response.status_code}")
