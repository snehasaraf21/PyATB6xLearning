import pytest
import allure
import requests


@allure.title("TC#1-Verify the GET requests")
@allure.description("Verify gthat the get request is working")
@pytest.mark.positive
def test_GET_requests_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response = requests.get(url=url)
    assert response.status_code == 200



@allure.title("TC#2-Verify the GET requests")
@allure.description("Verify that the get request is working")
@pytest.mark.negative
def test_GET_requests_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response = requests.get(url=url)
    assert response.status_code == 404