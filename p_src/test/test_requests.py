# Third-party imports...
from unittest.mock import Mock, patch
from nose.tools import assert_true, assert_is_not_none, assert_is_none, assert_list_equal
import requests
from test.index import get_todos


"""
nosetests --verbosity=2 test
"""


def test_request_response_v1():
    # Send a request to the API server and store the response.
    response = requests.get('http://jsonplaceholder.typicode.com/todos')
    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)


def test_request_response_v2():
    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)


@patch('test.index.requests.get')
def test_getting_todos_when_response_is_ok(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]
    # Configure the mock to return a response with an OK status code. Also, the mock should have
    # a `json()` method that returns a list of todos.
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos
    # Call the service, which will send a request to the server.
    response = get_todos()
    # If the request is sent successfully, then I expect a response to be returned.
    assert_list_equal(response.json(), todos)


@patch('test.index.requests.get')
def test_getting_todos_when_response_is_not_ok(mock_get):
    # Configure the mock to not return a response with an OK status code.
    mock_get.return_value.ok = False
    # Call the service, which will send a request to the server.
    response = get_todos()
    # If the response contains an error, I should get no todos.
    assert_is_none(response)

