import requests

import requests
url=" http://59.77.64.130/eportal/InterFace.do?method=login"
data = {
"userId": 账号,
"password": 密码,
"service": "lydx",
"queryString": "响应体"
}
r = requests.post(url,data=data).status_code
print(r)


'''
    Response.status_code	检查请求是否成功	200 代表正常，404 代表网页不存在。
    Response.encoding	定义编码	如果编码不对，网页就会乱码的。
    Response.content	把数据转成二进制	用于获取图片、音频类的数据。
    Response.text	把数据转为字符串	用于获取文本、网页原代码类的数据。
    
    requests.request()	构造一个请求，支持以下各种方法
    requests.get()	获取html的主要方法
    requests.head()	获取html头部信息的主要方法
    requests.post()	向html网页提交post请求的方法
    requests.put()	向html网页提交put请求的方法
    requests.patch()	向html提交局部修改的请求
    requests.delete()	向html提交删除请求
    
    r.status_code	http请求的返回状态，若为200则表示请求成功。
    r.text	http响应内容的字符串形式，即返回的页面内容
    r.encoding	从http header 中猜测的相应内容编码方式
    r.apparent_encoding	从内容中分析出的响应内容编码方式（备选编码方式）
    r.content	http响应内容的二进制形式
    
'''
