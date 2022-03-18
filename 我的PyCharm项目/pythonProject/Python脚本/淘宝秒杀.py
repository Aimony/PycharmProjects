# #淘宝模拟登陆采集阿里商品
# # -*- coding: utf-8 -*-
# #20200302 by 微信：huguo00289
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import datetime
#
# #定义一个taobao类
# class taobao_infos:
#
#     #对象初始化
#     def __init__(self):
#         url='https://login.taobao.com/member/login.jhtml'
#         self.url=url
#
#         options=webdriver.ChromeOptions() #配置 chrome 启动属性
#         #options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) #不加载图片，加快访问速度
#         options.add_experimental_option("excludeSwitches",['enable-automation']) # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
#
#         self.browser=webdriver.Chrome(executable_path=chromedriver_path,options=options)
#         self.wait=WebDriverWait(self.browser,10) #超时时长为10s
#
#     #扫码登陆淘宝
#     def login(self):
#         #打开网页
#         self.browser.get(self.url)
#         time.sleep(1)
#         time.sleep(15)
#
#
#     #打开抢购商品首页
#     def get_shop(self,shop_url,buytime):
#         print("正在打开需要抢购的页面")
#         self.browser.get(shop_url)
#         while True:
#             now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             if now > buytime:
#                 try:
#                     #等待购买按钮出现
#                     linkbuy=self.wait.until(EC.presence_of_element_located((By.ID,'J_LinkBuy')))
#                     linkbuy.click()
#                     sutj=self.wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="wrapper"]/a')))
#                     sutj.click()
#                     print(f"抢购成功，请尽快付款")
#                 except:
#                     self.browser.refresh()  # 刷新页面
#                     linkbuy = self.wait.until(EC.presence_of_element_located((By.ID, 'J_LinkBuy')))
#                     linkbuy.click()
#                     sutj = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="wrapper"]/a')))
#                     sutj.click()
#                     print(f"抢购成功，请尽快付款")
#
#
#
#
#
#     def gb(self):
#         print(">>> 抢购完毕，关闭浏览器！")
#         self.browser.quit()
#
#
# if __name__ == '__main__':
#     chromedriver_path = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36\chromedriver.exe"  #谷歌chromedriver完整路径
#     spider=taobao_infos()
#     spider.login()
#     datetime='2020-03-02 11:59:58'
#     shop_url="https://detail.tmall.com/item.htm?id=550189462849&price=24.8"
#     #shop_url='https://detail.tmall.com/item.htm?id=612510400743' #抢购商品页
#     try:
#         spider.get_shop(shop_url,datetime)
#     except:
#         spider.get_shop(shop_url, datetime)
#     spider.gb()





import time
from selenium import webdriver
import datetime

class Spider:
    def __init__(self, url):
        self.__base_url = url
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }
    def get_url(self):
        global driver
        driver.get(self.__base_url)
    def login(self):
        global driver
        if driver.find_element_by_link_text("亲，请登录"):
            driver.find_element_by_link_text("亲，请登录").click()
            print("请在30秒内扫描登陆")
            time.sleep(30)
            driver.get("https://cart.taobao.com/cart.htm")
    def selectAll(self,method):
        global driver
        # 打开购物车列表页面
        driver.get("https://cart.taobao.com/cart.htm")
        time.sleep(3)

        # 是否全选购物车
        if method == 0:
            while True:
                try:
                    if driver.find_element_by_id("J_SelectAll1"):
                        driver.find_element_by_id("J_SelectAll1").click()
                        break
                except:
                    # print(f"找不到购买按钮")
                    pass
        if method ==1 :
            print(f"请手动勾选需要购买的商品")
            time.sleep(30)

    def buy(self,times):
        global driver
        while True:
            now = datetime.datetime.now()
            # 对比时间，时间到的话就点击结算
            if now > times:
                # 点击结算按钮
                while True:
                    try:
                        if driver.find_element_by_link_text("结 算"):
                            driver.find_element_by_link_text("结 算").click()
                            print(f"结算成功，准备提交订单")
                            break
                    except:
                        pass
                # 点击提交订单按钮
                while True:
                    try:
                        if driver.find_element_by_link_text('提交订单'):
                            driver.find_element_by_link_text('提交订单').click()
                            print(f"抢购成功，请尽快付款")
                    except:
                        # print(f"再次尝试提交订单")
                        pass
                time.sleep(0.01)


option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)
spider = Spider("https://www.taobao.com")
spider.get_url()
spider.login()
#设置0为全选、1为手动
spider.selectAll(0)
# 设置抢购时间
set_time = datetime.datetime(2021,10,29,0,0)
spider.buy(set_time)