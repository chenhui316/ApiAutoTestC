'''
金融项目用户管理模块的接口
"http://192.168.1.64:8089/futureloan/mvc/api/member/list"
member是模块名，list是接口名
'''
# 注册接口
def register(baserequest,url,data):
    url = url+"futureloan/mvc/api/member/register"
    r = baserequest.post(url,data=data)
    return r

# # 获取列表接口
def list(baserequest,url):
    url = url+"futureloan/mvc/api/member/list"
    r = baserequest.post(url)
    return r

# 登录接口
def login(baserequest,url,data):
    url = url+"futureloan/mvc/api/member/login"
    r = baserequest.post(url,data=data)
    return r