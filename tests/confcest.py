import json 
import pytest

@pytest.fixture(scope="session")
def httpserver_listen_address():
    # set up in httpserver for the testing session
    return ("localhost", 443)

@oytest.fixture()
def httpserver_custom(httpserver):
    # get the expected request and response for the httpserver
    def set_httpserver(endpoint: str, response_data: str, status_code: int, data=None, content_type="application/json"):
        # the callable function to returned by the fixture
        if data is None:
            httpserver.expect_ordered_request(endpoint).respond_with_data(response_data=response_data,
                                                                          status=status_code,
                                                                          content_type=content_type)
        else:
             httpserver.expect_ordered_request(endpoint, data=data).respond_with_data(response_data=response_data,
                                                                                      status=status_code,
                                                                                      content_type=content_type)
    return set_httpserver

@pytest.fixture()
def httpserver_oauth2():
    #set up server for get bearer token request
    def set_httpserver_for_oauth2(response_data: str, status_code: int):

        # the callable will return by the fixture
        
        httpserver_custom(endpoint="/oauth2/token?grant_type=client_credentials",
                          response_data=response_data, 
                          status_code=status_code)
        
    return set_httpserver_for_oauth2