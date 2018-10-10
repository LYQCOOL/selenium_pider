# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/8 14:50'
from selenium import webdriver
import urllib

browser = webdriver.Chrome()
browser.get('https://weibo.com/')
import time
time.sleep(10)
username = browser.find_element_by_css_selector('#loginname')
passwd=browser.find_element_by_css_selector('input[node-type="password"]')
if username:
    username.send_keys('15283251646')
else:
    print('未找到用户名输入框！！！标签错误')
if passwd:
    passwd.send_keys('112358')
else:
    print('未找到密码输入框！！！标签错误')
yanzhengma=browser.find_element_by_css_selector('.code.W_fl img')
if yanzhengma:
    #获取验证码图片下载地址并下载到本地
    img_url=yanzhengma.get_attribute('src')
    data = urllib.request.urlopen(img_url).read()
    f = open('weibo.png' , 'wb')
    f.write(data)
    f.close()
    code_input=browser.find_element_by_css_selector('input[node-type="verifycode"]')
    browser.save_screenshot('E://pyCharm文档/Scrapy_Bobby/article_spiderarticle_spider/utils/weibo.png')
    codes=input('请输入截图里的验证码：')
    code_input.send_keys(codes)
browser.find_elements_by_css_selector('a[node-type="submitBtn"]')[0].click()

