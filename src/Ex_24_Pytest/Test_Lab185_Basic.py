import pytest

@pytest.mark.smoke
def test_method():
    print("Hello World ")
    assert 1 +1 == 2

@pytest.mark.regression
def test_login():
    print("Hello World ")
    assert 1 + 1 == 1
