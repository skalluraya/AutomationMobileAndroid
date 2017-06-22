'''
Created on Jun 21, 2017

@author: Shrikanth
'''
import unittest
from Factory import Factory


#This class is a base class for all testcase
class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = Factory().driver;
 
        
    @classmethod
    def setUpClass(cls):
        if Factory().driver == None:
            Factory().createAppiumDriver();

    @classmethod
    def tearDownClass(cls):
        Factory().driver.quit()
 
    
    
