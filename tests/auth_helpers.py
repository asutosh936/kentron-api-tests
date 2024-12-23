import requests


def get_auth_token():
    """Generates an authentication token."""
    url = "https://backend-dev.kentron.ai/api/v1/auth/login/"
    credentials = {"email": "dishant@mangotech.com",
                   "password": "hello",
                   "tenant_name": "mangotech"}
    response = requests.post(url, json=credentials)
    if response.status_code == 200:
        print('Get Auth Token %s ', response.json())
        return response.json().get('data').get('access')
    raise Exception(f"Authentication failed! Status code: {response.status_code}")
