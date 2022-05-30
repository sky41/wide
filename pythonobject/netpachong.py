import requests
import sqlite3

def requests52():
    r = requests.get('https://www.baidu.com/')
    r.status_code

    r.text
    print(r.status_code)
    if r.status_code == 418:
        print("sbai")
    else:
        print("l")
        print(r.text)
requests52()

def sqlite3tiao():
    conn = sqlite3.connect('cheshi.db')
    c = conn.cursor()
    print("数据库打开成功")



sqlite3tiao()


