from selenium import webdriver
import time

uname = ''
pwd = ''

drive = webdriver.Chrome()

drive.get('http://www.jd.com')

drive.find_element_by_link_text('请登录').click()
drive.find_element_by_link_text('登录').click()
drive.find_element_by_name('loginname').send_keys(uname)
drive.find_element_by_name('loginpwd').send_keys(pwd)
drive.find_element_by_id('loginsubmit').click()
time.sleep(3)
drive.get('https://cart.jd.com/cart.action')
drive.find_element_by_link_text('去结算').click()