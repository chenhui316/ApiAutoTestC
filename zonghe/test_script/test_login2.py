import pytest

from zonghe.baw import Member
from zonghe.caw import MySqlOp
from zonghe.caw.DataRead import read_yaml

from ApiAutoTest.zonghe.caw import Check


@pytest.fixture(params=read_yaml(r"\test_data\login.yaml"))
def login_data(request):
    return request.param


def test_login(login_data,baserequest,url,db_info):
    #注册用户
    MySqlOp.delete_user(db_info, login_data['regdata']['mobilephone'])
    Member.register(baserequest,url,login_data['regdata'])
    print("注册数据：",login_data['regdata'])
    #登录
    r = Member.login(baserequest,url,login_data['logindata'])
    print("登录数据：",login_data['logindata'])
    # assert r.json()['code'] == login_data['expect']['code']
    # assert r.json()['status'] == login_data['expect']['status']
    # assert r.json()['msg'] == login_data['expect']['msg']
    Check.equal(r.json(),login_data['expect'],'code,status,msg')
    MySqlOp.delete_user(db_info, login_data['logindata']['mobilephone'])
