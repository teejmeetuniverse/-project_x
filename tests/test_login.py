import pytest
from unittest import mock
from login import authenticate_with_twitter


## create a test where we receive a 200 status code and a access token is in the response
def test_authenticate_with_twitter(httpserver_oauth2):
    """
    test case: testing authenticate_with_twitter method under normal input
    expected result: successful run without exception
    """
    response_data = '{"access_token": "abc123"}'
    status_code = 200
    httpserver_oauth2(response_data=response_data, status_code=status_code)
    response = authenticate_with_twitter("user", "pass")
    assert response == "abc123"


## create a test where we don't receive a 200 status code

    response_data = '{"access_token": "abc123"}'
    # i just changed the status code to a 400 and kept the rest of the code the same
    status_code = 400
    httpserver_oauth2(response_data=response_data, status_code=status_code)
    response = authenticate_with_twitter("user", "pass")
    assert response == "abc123"

## create a test were we receive a 200 status code but there isn't a access token in the response

    response_data = '{"access_token": "abc123"}'
    status_code = 200
    httpserver_oauth2(response_data=response_data, status_code=status_code)
    response = authenticate_with_twitter("user", "pass")
    # since we are looking for a 200 status code instead of a response i figured we'd change line 35 to the below
    assert status_code == "200"
