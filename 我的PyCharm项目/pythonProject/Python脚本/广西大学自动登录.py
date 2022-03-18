import requests
from sys import exit

username = '填入学号'
password = '填入密码'
route = '填入运营商：校园网/中国移动/中国联通/中国电信'


def WIFI_is_connected():
    from os import popen
    import re

    output = popen('netsh WLAN show interfaces').read()
    pattern = 'SSID\s+\:\s.+'
    search_object = re.search(pattern, output)
    if search_object:
        SSID = search_object.group().split(':')[-1].strip()
        return SSID == 'GXU-WLAN'
    else:
        return False


def ping_success():
    from requests.exceptions import ConnectTimeout
    try:
        requests.get("https://www.baidu.com", timeout=1)
        return True
    except ConnectTimeout:
        return False


def good_response(r):
    """
    根据发出的认证请求得到的response判断是否认证成功
    :param r: 发出的认证请求得到的response
    :return: 是否认证成功
    """
    return '<title>认证成功页</title>' in r.text


def certificate():
    routes = {
        '校园网': '',
        '中国电信': 'telecom',
        '中国移动': 'cmcc',
        '中国联通': 'unicom'
    }
    response_ = requests.get('http://172.17.0.2:801/eportal', params={
        'c': 'ACSetting',
        'a': 'Login',
        'loginMethod': '1',
        'protocol': 'http:',
        'hostname': '172.17.0.2',
        'iTermType': '1',
        'wlanacname': 'ME60-1',
        'vlanid': '0',
        'ip': '172.18.17.23',
        'enAdvert': '0',
        'jsVersion': '2.4.3',
        'DDDDD': f',0,{username}@{routes[route]}',  # 0代表电脑端1代表手机、ipad端
        'upass': password,
        'R1': '0',  # r1r2r3应该是选择登录的渠道校园网移动联通电信自己可以测试0为校园网
        'R2': '0',
        'R3': '0',
        'R6': '0',
        'para': '00',
        '0MKKey': '123456'
    }, timeout=2)
    return response_


if __name__ == '__main__':
    if ping_success():
        print('校园网认证成功，现在可以上网了！', end='')
        exit()
    if WIFI_is_connected():
        response = certificate()
        if good_response(response):
            print('校园网认证成功，现在可以上网了！', end='')
        else:
            if ping_success():
                print('校园网认证成功，现在可以上网了！', end='')
            else:
                print('校园网认证失败', end='')

    else:
        print('请先连接校园网WIFI', end='')