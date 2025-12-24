import pytest
import allure

@allure.title("verify that the create booking is working.")
@allure.description("we are going to Verify create booking is working in the future of this function.")
@pytest.mark.positive
def test_create_booking_positive():
    print("test1")
    assert 1-1 == 2

@allure.title("verify that the create booking, with invalid data is working.")
@allure.description("this Testcasse check for the negative create booking")
@pytest.mark.negative
def test_create_booking_negative_1():
    print("test2")
    assert 1+1 == 2

@allure.title("verify that the create booking, with invalid data is working.")
@allure.description("this Testcasse check for the negative create booking")
@pytest.mark.negative
def test_create_booking_negative_2():
    print("test2")
    assert 1+1 == 2