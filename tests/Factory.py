'''
Created on Jun 21, 2017

@author: Shrikanth
'''
from SingletonDecorator import singleton
import os
from appium import webdriver
import Utils


#Factory Class is used to create session objects like driver
@singleton
class Factory(object):
    def __init__(self):
        self.driver = None
    
    def createAppiumDriver(self):
        "Setup for the test"
        device_id = Utils.find_device_id()
        if device_id == None:
            #handle error case
            device_id = 'df53043f'
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = device_id
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'../apps/ApiDemos.apk'))
        desired_caps['appPackage'] = 'com.github.axet.android.apis'
        desired_caps['appActivity'] = '.ApiDemos'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)