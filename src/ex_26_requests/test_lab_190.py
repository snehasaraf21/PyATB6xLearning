import pytest
import allure
import requests

@allure.title("TC1 - Create Booking CRUD Positive")
@allure.description("Verify the create Booking!")
#@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path


    headers = {
        "content-type": "application/json"
    }

    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=full_url, headers=headers, json=payload)
    assert response_data.status_code == 200
    response_data_json = response_data.json()
    print(response_data_json)

    # to fetch booking id >0 and firstname =="Jim"
    bookingId = response_data_json["bookingid"]
    print("booking Id:",bookingId)
    firstname = response_data_json["booking"]["firstname"]
    lastname = response_data_json["booking"]["lastname"]
    print("firstname and lastname",firstname, lastname)

    assert bookingId is not None
    assert bookingId > 0
    assert type(bookingId) == int

    assert firstname == "Jim"
    assert type(lastname) == str


    lastname = response_data_json["booking"]["lastname"]
    totalprice = response_data_json["booking"]["totalprice"]
    depositpaid = response_data_json["booking"]["depositpaid"]

    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True




@allure.title("TC2 - Create Booking CRUD Negative")
@allure.description("Verify that invid payload is not working!")
#@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {
        "content-type": "application/json"
    }
    payload = {}
    response = requests.post(url=url, headers=headers, json=payload)
    assert response.status_code == 200
    assert response.text == "Internal server error"
