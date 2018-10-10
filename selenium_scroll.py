# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/8 15:44'
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.oschina.net/blog')
#执行js代码
for i in range(3):
    browser.execute_script(
        "window.scrollTo(0,document.body.scrollHeight); var lenofPage=document.body.scrollHeight; return lenofPage;")
    time.sleep(3)