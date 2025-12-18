import pytest
import requests
import allure

def test_create_token():
    base_url = "https://restful-booker.herokuapp.com"
    headers ={
        "Content-Type": "application/json",
        "Accept": "application/json", }
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }
    response_data = requests.post(full_url, json=json_payload_auth, headers=headers)
    print(response_data)
    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json['token']
    print(token)
    assert type(token) == str
    assert len(token) > 0
