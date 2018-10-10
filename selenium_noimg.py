# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/8 16:06'
from selenium import webdriver
import time
#设置chromedriver不加载图片,加速页面的加载
option=webdriver.ChromeOptions()
prefs={'profile.managed_default_content_settings.images':2}
option.add_experimental_option("prefs",prefs)
browser=webdriver.Chrome(chrome_options=option)
browser.get('https://www.taobao.com/')


