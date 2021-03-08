import pytest

from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests


@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(r"\test_env\env.ini", "url")

@pytest.fixture(scope='session')
def db_info():
    return eval(DataRead.read_ini(r"\test_env\env.ini", "db_info"))

@pytest.fixture(scope='session')
def baserequest():
    return BaseRequests()