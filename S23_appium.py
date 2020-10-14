# coding=utf-8

from appium import webdriver

desired_caps = {
  'platformName': 'Android',
  'deviceName': '6HJDU19926001629',#来自于adb devices命令
  'platformVersion': '10',#这个应该是安卓版本吧
  'appPackage': 'com.tencent.mm',
  'appActivity': 'com.tencent.mm.ui.LauncherUI'
 }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)