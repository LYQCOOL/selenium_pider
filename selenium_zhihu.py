# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/8 14:33'
from selenium import webdriver
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/signin')
phone=browser.find_elements_by_css_selector('.SignFlow-accountInput.Input-wrapper .Input')
passwd=browser.find_elements_by_css_selector('.SignFlow-password .Input')
phone[0].send_keys('17738722825')
passwd[0].send_keys('lyq11235811')