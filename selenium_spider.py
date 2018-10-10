# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/8 14:01'
from selenium import webdriver
from scrapy.selector import Selector
# 打开谷歌浏览器
# 若没将浏览器Chrome的exe文件添加到PATH下，则带参数指定浏览exe文件的位置
# brower=webdriver.Chrome(executable_path='....')
# 添加在PATH下自动找取
brower = webdriver.Chrome()
# 获取的是js和css文件加载完后的网页，而不是该网页源代码

brower.get('https://www.baidu.com/')
# 获取js和css加载完后的网页
print(brower.page_source)
'''
  selenium提供了很多提取网页内容的方法，如下等，但是selenium是用纯python写的，
  提取效率慢，若知是提取内容，建议用scrapy，模拟输入密码和点击时用selenium的方法
  brower.find_element_by_css_selector()
  brower.find_elements_by_css_selector()
  ......
'''
#利用scrapy的selector解析，速度更快
t_select=Selector(text=brower.page_source)
# 退出
brower.quit()
