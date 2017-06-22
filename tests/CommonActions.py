'''
Created on Jun 21, 2017

@author: Shrikanth
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#This class defines all the common actions of the driver
class CommonActions:
    def __init__(self, driver):
        self.driver = driver
        
    def findElement(self, xpath, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    
    def findElements(self, xpath, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath)))
        
    def click(self, element):
        element.click()
    
    def back(self):
        self.driver.back()