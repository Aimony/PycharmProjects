import cgitb

import requests
from lxml import etree


a = requests.get("https://weibo.com/")
# print(a.text)
x = etree.HTML(a.text)
m = x.xpath('//*[@id="app"]/div[1]/div[2]/div[1]/div/div/h2/text()')
for i in m:
    print(i)

