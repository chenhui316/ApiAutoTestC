# assert r.json()['code'] == login_data['expect']['code']
# assert r.json()['status'] == login_data['expect']['status']
# assert r.json()['msg'] == login_data['expect']['msg']
from pytest_check import check


def equal(real,expect,keys):
    ks = keys.split(',')
    for k in ks:
        r = str(real.get(k))
        e = str(expect.get(k))
        try:
            check.equal(r,e)
            print(f"检验{k}成功")
        except Exception as e:
            print(f"检验{k}失败，失败信息为{e}")