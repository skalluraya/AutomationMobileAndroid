'''
Created on Jun 21, 2017

@author: Shrikanth
'''
from BaseScreen import BaseScreen

#This Page class for Home screen
class HomeScreen(BaseScreen):
    def __init__(self, unit_test_case):
        BaseScreen.__init__(self, unit_test_case)
        self.verifyScreenTitle('API Demos 17')
    
    def enterSection(self, sectionName):
        listSectionName = self.actions.findElement("//*[contains(@resource-id,'android:id/list')]//android.widget.TextView[@text='"+sectionName+"']")
        self.actions.click(listSectionName)
    
    def verifyListElements(self):
        list_elements = self.actions.findElements("//*[contains(@resource-id,'android:id/list')]//android.widget.TextView")
        self.unit_test_case.assertTrue(len(list_elements)>0)
        self.unit_test_case.assertEqual('Accessibility', list_elements[0].text)
    
    def goBackToHomeScreen(self):
        self.actions.back()