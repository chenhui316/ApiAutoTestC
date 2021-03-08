import pytest

from ApiAutoTest.zonghe.caw.DataRead import read_yaml


@pytest.fixture(params=read_yaml(r"\test_data\recharge.yaml"))
def recharge_data(request):
    return request.param

def test_recharge():
    pass
#注册

#登录

#充值