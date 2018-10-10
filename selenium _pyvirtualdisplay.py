# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/10 16:52'
from selenium import webdriver
from pyvirtualdisplay import Display
#设置无界面，windows环境下不适用
display=Display(visible=0,size=(800,600))
display.start()
browser=webdriver.Chrome()
browser.get('https://i.cnblogs.com/EditPosts.aspx?postid=9753969&update=1')
browser.quit()
display.stop()