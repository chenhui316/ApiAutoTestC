'''
操作数据库的方法
'''
import pymysql


def connect(db_info):
    host = db_info['host']
    port = db_info['port']
    user = db_info['user']
    pwd = db_info['pwd']
    database = db_info['name']
    try:
        conn = pymysql.connect(host=host,
        port=port,
        user=user,
        password=pwd,
        database=database,
        charset="utf8")
        print("连接数据成功")
        return conn
    except Exception as e:
        print(f"数据库连接失败,异常信息为：{e}")


def disconnect(conn):
    try:
        conn.close()
        print("数据库断开成功")
    except Exception as e:
        print(f"数据库连接失败,异常信息为：{e}")


def execute(conn,sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"执行sql语句失败，异常信息为{e}")


def delete_user(db_info,mobilephone):
    '''
    :param db_info:
    :param mobilephone:
    :return:
    '''
    conn = connect(db_info)
    execute(conn,f"delete from member where mobilephone = {mobilephone};")
    disconnect(conn)


if __name__ == '__main__':
    db_info = {"host":"192.168.1.64","port":3306,"name":"apple","user":"root","pwd":"123456"}
    delete_user(db_info,"13995917432")