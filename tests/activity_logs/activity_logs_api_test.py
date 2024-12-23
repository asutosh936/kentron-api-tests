import requests


def test_successful_activity_logs(auth_token, base_url):
    url = f"{base_url}/activity-logs/?page=1&page_size=100&entity=Workspace"
    headers = {"Authorization": f"Bearer {auth_token}",
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200


def test_un_successful_activity_logs_with_missing_authorization(base_url):
    url = f"{base_url}/activity-logs/?page=1&page_size=100&entity=Workspace"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 401


def test_un_successful_activity_logs_with_invalid_authorization(base_url):
    url = f"{base_url}/activity-logs/?page=1&page_size=100&entity=Workspace"
    headers = {"Authorization": "Bearer abcdefghijklmnopqrstuvwxyz",
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 401


def test_un_successful_activity_logs_with_invalid_workspace(auth_token, base_url):
    url = f"{base_url}/activity-logs/?page=1&page_size=100&entity=Workspace1"
    headers = {"Authorization": f"Bearer {auth_token}",
               "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 400
