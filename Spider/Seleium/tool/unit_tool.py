import requests
from Spider.Seleium.msg_xpath.dialog import *
from bs4 import BeautifulSoup
from lxml import etree


def get_html(url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text


def bs4Msg(msg):
    bs4_pos = BeautifulSoup(msg, 'lxml')
    return bs4_pos.find_all(bs4_index[0], style=bs4_index[1])


# 有附件的情况，通过正则表达式寻找附件编号
def getFile(msg):
    alist = msg.find_all('a')
    ret = []
    for a in alist:
        ret.append(a['id'])
    return ret


# bs4类型转字符串
def bs4ToStr(bs4):
    msg = []
    for item in bs4:
        msg.append(item.text)
    return msg


# 判断招标是否有附件
def haveFile(msg):
    for item in msg:
        if item == '附件：':
            return True
    return False


# 将列表拆分成两个
def splitList(msg):
    head = []
    _val = []
    tag = 0
    for item in msg:
        if item in overlap:
            continue
        if tag % 2 == 0:
            head.append(item)
        else:
            _val.append(item)
        tag += 1
    return [head, _val]


# 向列表补充文件连接信息
def insertFile(file_url, _val):
    # print(type(file_url), len(file_url), type(_val), len(_val))
    pos = len(_val) - len(file_url)
    cur = 0
    while pos < len(_val):
        old = _val[pos]
        _val[pos] = '(' + download_root + file_url[cur] + ')' + old
        cur += 1
        pos += 1


def findCity(_val):
    print("before", _val)
    pos = 0
    for province in provinces:
        if pos == time_pos:
            pos += 1
            continue
        if _val[city_pos].find(province) != -1:
            _val[city_pos] = province
            print(_val)
            return
        pos += 1

    pos = 0

    key = {}
    for msg in _val:
        if pos == time_pos:
            pos += 1
            continue
        for city in cities:
            for item in city:
                if msg.find(item) != -1:
                    print(city, msg, item)
                    if cities[city] in key:
                        print('debug')
                        key[cities[city]] += 1
                    else:
                        key[cities[city]] = 1
        pos += 1
    print(key)
    if len(key) != 0:
        _val[city_pos] = max(key.items(), key=lambda x: x[1])[0]
    else:
        _val[city_pos] = '未知区域'
        print(key)
    print(_val)
