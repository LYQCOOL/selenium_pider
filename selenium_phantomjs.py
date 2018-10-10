# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/9 21:25'
from selenium import webdriver

browser = webdriver.PhantomJS(executable_path='E:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
browser.get('https://www.cnblogs.com/lyq-biu/p/9753969.html')
print(browser.page_source)
