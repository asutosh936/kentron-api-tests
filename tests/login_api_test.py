import requests
import os


def test_successful_login(base_url):
    """Test Successful Login with Valid Credentials."""
    url = f"{base_url}/auth/login/"
    headers = {"Content-Type": "application/json"}
    payload = {"email": os.getenv("USER_EMAIL"),
               "password": os.getenv("USER_PASSWORD"),
               "tenant_name": os.getenv("USER_TENANT")}
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["error"] == False
    assert response.json()["message"] == "Login Success"


def test_un_successful_login_with_invalid_credentials(base_url):
    """Test Unsuccessful login with invalid credentials."""
    url = f"{base_url}/auth/login/"
    headers = {"Content-Type": "application/json"}
    payload = {"email": "dishant1@mangotech.com",
               "password": "hello1", 
               "tenant_name": "mangotech1"}
    response = requests.post(url, json=payload, headers=headers)
    print(response.json().get("errors").get("non_field_errors"))
    assert response.status_code == 400
    assert response.json().get("errors").get("non_field_errors") == ['Tenant with this name does not exist.']


def test_un_successful_login_with_missing_email(base_url):
    """Test Unsuccessful login with missing email."""
    url = f"{base_url}/auth/login/"
    headers = {"Content-Type": "application/json"}
    payload = {"email": "", "password": "hello", 
               "tenant_name": "mangotech"}
    response = requests.post(url, json=payload, headers=headers)
    print(response.json().get("errors").get("non_field_errors"))
    assert response.status_code == 400
    assert response.json().get("errors") != None
    assert response.json().get("errors").get("email") == ['This field may not be blank.']


def test_un_successful_login_with_missing_password(base_url):
    """Test Unsuccessful login with missing email."""
    url = f"{base_url}/auth/login/"
    headers = {"Content-Type": "application/json"}
    payload = {"email": "dishant@mangotech.com", "password": "", 
               "tenant_name": "mangotech"}
    response = requests.post(url, json=payload, headers=headers)
    print(response.json().get("errors").get("non_field_errors"))
    assert response.status_code == 400
    assert response.json().get("errors") != None
    assert response.json().get("errors").get("password") == ['This field may not be blank.']


def test_un_successful_login_with_missing_tenant(base_url):
    """Test Unsuccessful login with missing Tenant."""
    url = f"{base_url}/auth/login/"
    headers = {"Content-Type": "application/json"}
    payload = {"email": "dishant@mangotech.com", "password": "hello", 
               "tenant_name": ""}
    response = requests.post(url, json=payload, headers=headers)
    print(response.json().get("errors").get("non_field_errors"))
    assert response.status_code == 400
    assert response.json().get("errors") != None
    assert response.json().get("errors").get("tenant_name") == ['This field may not be blank.']