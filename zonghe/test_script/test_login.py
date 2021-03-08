import pytest

from zonghe.baw import Member
from zonghe.caw import MySqlOp
from zonghe.caw.DataRead import read_yaml



@pytest.fixture(params=read_yaml(r"\test_data\login_setup_data.yaml"))
def login_setup_data(request):
    return request.param

@pytest.fixture(params=read_yaml(r"\test_data\login_data.yaml"))
def login_data(request):
    return request.param




@pytest.fixture(params=read_yaml(r"\test_data\login_setup_data.yaml"))
def register(login_setup_data,baserequest,url,db_info):
    #注册用户
    MySqlOp.delete_user(db_info, login_setup_data['data']['mobilephone'])
    Member.register(baserequest,url,login_setup_data['data'])
    yield
    #删除注册用户
    MySqlOp.delete_user(db_info, login_setup_data['data']['mobilephone'])

def test_login(register,login_data,baserequest,url):
    r = Member.login(baserequest,url,login_data['data'])
    print(r.text)
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['msg'] == login_data['expect']['msg']





