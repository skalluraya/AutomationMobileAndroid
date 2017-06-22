'''
Created on Jun 21, 2017

@author: Shrikanth
'''
from Factory import Factory
from CommonActions import CommonActions

#This class is a base class for all Page Class
class BaseScreen(object):

    def __init__(self, unit_test_case):
        self.driver = Factory().driver
        self.actions = CommonActions(Factory().driver)
        self.unit_test_case = unit_test_case
        
        
    def verifyScreenTitle(self, title):
        titleXpath = "//android.widget.TextView[contains(@resource-id,'action_bar_title')]"
        element = self.actions.findElement(titleXpath)
        self.unit_test_case.assertEqual(title, element.text)