import pytest
import requests
import allure

@allure.title("TC#1 verify if 2-2 ==0" )
@allure.description("This is a basic math test")
@pytest.mark.positve
def test_basic_math():
    assert 2 - 2 == 0

@allure.title("TC#1 verify if 3-3 ==0" )
@allure.description("This is a basic math test")
@pytest.mark.positve
def test_basic_math2():
    assert 3 - 3 == 0


@pytest.mark.skip(reason="This is not working")
def test_basic_math3():
    assert 0 -0 != 0