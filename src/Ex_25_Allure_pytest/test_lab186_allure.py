import pytest
import allure


@allure.title("Verify that create booking is working")
@allure.description("WE are going to verify create booking is working in future ")
@pytest.mark.positive
def test_create_booking_positive():
    print("TC1")
    assert 1+1 == 2


@allure.title("Verify that create booking is working")
@allure.description("WE are going to verify create booking is working in future ")
@pytest.mark.positive
def test_create_booking_positive2():
    print("TC1")
    assert 1 + 2 == 3


@allure.title("Verify that create booking is working")
@allure.description("WE are going to verify create booking is working in future ")
@pytest.mark.negative
def test_create_booking_negative():
    print("TC2")
    assert 1+1 == 1


@allure.title("Verify that create booking is working")
@allure.description("WE are going to verify create booking is working in future ")
@pytest.mark.negative
def test_create_booking_negative2():
    print("TC3")
    assert 1+1 == 3