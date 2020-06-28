import pytest


@pytest.fixture
def csv_file():
    return "csv file!!!"


def pytest_addoption(parser):
    """
    test with pytest fixture
    """
    parser.addoption('--os-name', default='linux', help='OS Name')
